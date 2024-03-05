
import re
import streamlit as st
import os
import boto3
import json
import base64
from PIL import Image
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


st.set_page_config(page_title="Insurance Claim - Car Damage Image Search", layout="wide")
st.title("Auto Insurance - Multimodal Search")
st.caption("Search public 'car damage' dataset")


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
    print(e)

# calls Amazon Bedrock to get a vector from either an image, text, or both


def get_multimodal_vector(input_image_base64=None, input_text=None):
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

# creates a vector from an image file


def get_vector_from_file(file_path):
    with open(file_path, "rb") as image_file:
        input_image_base64 = base64.b64encode(image_file.read()).decode('utf8')
    vector = get_multimodal_vector(input_image_base64=input_image_base64)
    return vector

# MDB database and collection


db = client['claim_resolution']
coll = db['car_damage_photos']

# Search with an image
uploads_dir = 'uploaded'
if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)

uploaded_file = st.file_uploader("Search with an image:", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_path = os.path.join(uploads_dir, uploaded_file.name)
    image.save(img_path)

    query_image = img_path
    image_folder = 'images'
    query_embedding = get_vector_from_file(query_image)

    # Make sure that the index name in this query matches with the one on Atlas
    documents = coll.aggregate([
      {"$vectorSearch": {
        "index": "claim_image_search",
        "path": "embedding",
        "queryVector": query_embedding,
        "numCandidates": 100,
        "limit": 10,
          }},
      {
           "$project": {
                "filename": 1,
                "data": 1,
                "embedding": 1,
                "score": {"$meta": "vectorSearchScore"}
            }
      }
    ])

    documents = list(documents)

    similar_images_list = []
    score_list = []

    for i in range(5):
        image_file = documents[i]['filename']
        image_path = os.path.join(image_folder, image_file)
        similar_images_list.append(image_path)
        score = documents[i]['score']
        score_list.append(score)

    # Display 3x3 grid
    st.image(query_image)
    st.write("Search Results:")
    cols = st.columns(3)
    for i in range(5):
        with cols[i % 3]:
            st.image(similar_images_list[i], width=256)
            st.write("Score: ", score_list[i])
            st.write("Severity: ", re.split("[_.]", documents[i]['filename'])[0][3:])

# Search with text
text_input = st.text_input('Search with text:')

if text_input:
    query_embedding = get_multimodal_vector(input_image_base64=None, input_text=text_input)
    image_folder = 'images'

    # Make sure that the index name in this query matches with the one on Atlas
    documents = coll.aggregate([
      {"$vectorSearch": {
        "index": "claim_image_search",
        "path": "embedding",
        "queryVector": query_embedding,
        "numCandidates": 100,
        "limit": 10,
          }},
      {
            "$project": {
                "filename": 1,
                "data": 1,
                "embedding": 1,
                "score": {"$meta": "vectorSearchScore"}
            }
      }
    ])

    documents = list(documents)

    similar_images_list = []
    score_list = []

    for i in range(5):
        image_file = documents[i]['filename']
        image_path = os.path.join(image_folder, image_file)
        similar_images_list.append(image_path)
        score = documents[i]['score']
        score_list.append(score)

    # Display 3x3 grid
    st.write("Search Results:")
    cols = st.columns(3)
    for i in range(5):
        with cols[i % 3]:
            st.image(similar_images_list[i], width=256)
            st.write("Score: ", score_list[i])
            st.write("Severity: ", re.split("[_.]", documents[i]['filename'])[0][3:])
