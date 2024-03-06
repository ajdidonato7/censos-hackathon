from faker import Faker
import random
import pymongo
from bson import ObjectId

fake = Faker()

client = pymongo.MongoClient("mongodb+srv://team5:team5password!@cluster0.iarvn.mongodb.net/")
db = client["claim_resolution"]
collection = db["car_damage_photos"]

companies = [
    "Toyota",
    "Ford",
    "Honda",
    "General Motors",
    "Nissan",
    "Subaru",
    "Tesla",
    "Mazda",
    "Chrysler",
    "Dodge",
    "Cadillac",
    "Lexus",
    "Audi"
]


results = collection.find({"severity": "severe"})

for result in results:
    claim_value = fake.random_int(min=10000, max=50000)
    collection.update_one(
        {
            "_id": result["_id"]
        },
        {'$set': {'claim_amount': claim_value}}
    )
    print("updated document with value ", claim_value)