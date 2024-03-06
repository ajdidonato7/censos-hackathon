import pymongo
from bson.json_util import dumps
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

client = pymongo.MongoClient("mongodb+srv://team5:team5password!@cluster0.iarvn.mongodb.net/")
db = client["claim"]
collection = db["Item"]

print(".......changestream started......")
# load environment variable
load_dotenv()
mongo_uri = os.getenv('MONGO_URI')
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')
aws_session_token = os.getenv('aws_session_token')

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


change_stream = collection.watch()
for change in change_stream:

    try:
        change_doc_id = change["fullDocument"]["_id"]
        print(change_doc_id)
        image = change["fullDocument"]["image"]["picture"]
        # import pdb; pdb.set_trace()
        # image = base64.b64decode(image)
        image = base64.b64encode(image)
        image = image.decode('utf-8')
        vector = get_multimodal_vector(input_image_base64=image)
        print("vector is ", vector)

        vector_db = client['claim_resolution']
        vector_coll = vector_db['car_damage_photos']

        documents = vector_coll.aggregate([ # add these documents to a field for the document that comes with change stream
        {
            "$vectorSearch": {
                "index": "claim_image_search",
                "path": "embedding",
                "queryVector": vector,
                "numCandidates": 100,
                "limit": 5,
            }
        }]
        )

        documents = list(documents)

        total = 0
        count = 0
        for document in documents:
            count += 1
            total += document["claim_amount"]

        average = total / count

        collection.update_one(
            {
                "_id": change_doc_id
            },
            {
                "$set": {
                    'claim_estimate': average,
                    'severity': documents[0]["severity"],
                    "matches": documents
                }
            }
        )
    except:
        print("error occurred")






