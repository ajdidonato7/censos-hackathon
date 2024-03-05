
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import boto3
import json
import base64
import matplotlib.pyplot as plt
from PIL import Image
import re


# load environment variable
load_dotenv()
mongo_uri = os.getenv('MONGO_URI')
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')
aws_session_token = os.getenv('aws_session_token')



# Create a new client and connect to the server
client = MongoClient(mongo_uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"An error occurred while connecting to MongoDB: {e}")


# Data visualization

def display_multiple_images(file_names):
    num_images = len(file_names)
    fig, axes = plt.subplots(1, num_images)
    fig.set_figwidth(5 * num_images)
    for ax, file_name in zip(axes, file_names):
        ax.imshow(Image.open(file_name))
        ax.axis("off")
    plt.show()


def display_single_image(file_name):
    fig, ax = plt.subplots(1, 1)
    fig.set_figwidth(3)
    ax.imshow(Image.open(file_name))
    ax.axis("off")
    plt.show()


# calls Amazon Bedrock to get a vector from either an image, text, or both
def get_multimodal_vector(input_image_base64=None, input_text=None):
    try:
        bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name="us-east-1",
            # Passing credentials during client creation
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token)

        request_body = {}
        if input_text:
            request_body["inputText"] = input_text
        if input_image_base64:
            request_body["inputImage"] = input_image_base64
        request_body["embeddingConfig"] = {"outputEmbeddingLength": 384}
        body = json.dumps(request_body)
        response = bedrock.invoke_model(
            body=body,
            modelId="amazon.titan-embed-image-v1",
            accept="application/json",
            contentType="application/json"
        )
        response_body = json.loads(response.get('body').read())
        embedding = response_body.get("embedding")
        return embedding
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# creates a vector from an image file path

def get_vector_from_file(file_path):
    with open(file_path, "rb") as image_file:
        input_image_base64 = base64.b64encode(image_file.read()).decode('utf8')

    vector = get_multimodal_vector(input_image_base64=input_image_base64)
    return vector


# embed query testing for an image
embeddings = get_vector_from_file('./images/01-minor_0001.JPEG') 
print(len(embeddings))   # length of embedding dimensions = 1 x 384
print(embeddings[:5])  # only include the first 5 elements of the embedding

# Vectorize dataset and load it to MongoDB Atlas

db = client['claim_resolution']
coll = db['car_damage_photos']

image_folder = 'images'

image_files = [
    f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))
]

for image_file in image_files:
    # Construct the full path to the image file
    image_path = os.path.join(image_folder, image_file)

    img_embedding = get_vector_from_file(image_path)
    severity = re.split("[_.]", image_file)[0]

    image_document = {
        'filename': image_file,
        # 'data': image_data,
        'embedding': img_embedding,
        'severity': severity[3:],
    }
    try:
        coll.insert_one(image_document)
        print(f"Inserted: {image_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Failed to insert: {image_file}")

print("All images inserted into MongoDB.")