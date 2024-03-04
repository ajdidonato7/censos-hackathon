from sentence_transformers import SentenceTransformer
from PIL import Image
import pymongo
from bson import json_util
            
connection = pymongo.MongoClient("mongodb+srv://team5:team5password!@cluster0.iarvn.mongodb.net/")
product_collection = connection["vector_search"]["damage"]
preTrainedModelName = "clip-ViT-L-14"
model = SentenceTransformer(preTrainedModelName)

input_image = Image.open("images/03-severe/0001.JPG")
vector_query = model.encode(input_image).tolist()
pipeline = [
    {
        "$search": {
            "index": "damage",
            "knnBeta": {
                "vector": vector_query,
                "path": "imageVector",
                "k": 10
            }
        }
    },
    {
        "$project": {
            "imageVector": {"$slice": ["$imageVector", 5]},
                "imageFile": 1,
            "price": 1,
            "discountPercentage": 1,
            "averageRating" : 1,
            "_id": 0,
            'score': {
                '$meta': 'searchScore'
            }
        }
    }
]

# Execute the pipeline
docs = list(product_collection.aggregate(pipeline))

# Return the results unders the docs array field
json_result = json_util.dumps({'docs': docs}, json_options=json_util.RELAXED_JSON_OPTIONS)

print(json_result)

