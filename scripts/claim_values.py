from faker import Faker
import random
import pymongo
from bson import ObjectId

fake = Faker()

client = pymongo.MongoClient("mongodb+srv://team5:team5password!@cluster0.iarvn.mongodb.net/")
db = client["claim_resolution"]
collection = db["car_damage_photos"]


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



# def generate_fake_document():
#     # Generate fake data for each field
#     INDEX_ID = fake.uuid4()
#     eid = fake.uuid4()
#     planConsumptionProcessed = random.choice([True, False])
#     validData = random.choice([True, False])
#     imsi = fake.random_int(min=1000000, max=999999999)
#     providerType = fake.random_element(elements=('Type A', 'Type B', 'Type C'))
#     cdrid = fake.uuid4()
#     pmn = fake.random_int(min=100, max=999)
#     clientUuid = fake.uuid4()
#     createdAt = fake.date_time_this_decade()
#     iccid = fake.random_int(min=10000000000, max=99999999999)
#     startTime = fake.date_time_this_decade()
#     stopTime = fake.date_time_this_decade()
#     totalUsage = fake.random_int(min=1, max=100)
#     msisdn = fake.random_int(min=1000000000, max=9999999999)
#     cdrFileName = fake.file_name(extension='cdr')
#     ipAddress = fake.ipv4()
#     connectionProfileUuid = fake.uuid4()
#     cellId = fake.random_int(min=100, max=999)
#     importUuid = fake.uuid4()
#     mccMnc = fake.random_int(min=100000, max=999999)
#     imei = fake.random_int(min=100000000, max=9999999999)
#     planEntryUndefined = random.choice([True, False])

#     # Create a dictionary representing the document
#     document = {
#         "INDEX_ID": INDEX_ID,
#         "eid": eid,
#         "planConsumptionProcessed": planConsumptionProcessed,
#         "validData": validData,
#         "imsi": imsi,
#         "providerType": providerType,
#         "cdrid": cdrid,
#         "pmn": pmn,
#         "clientUuid": clientUuid,
#         "createdAt": createdAt,
#         "iccid": iccid,
#         "startTime": startTime,
#         "stopTime": stopTime,
#         "totalUsage": totalUsage,
#         "msisdn": msisdn,
#         "cdrFileName": cdrFileName,
#         "ipAddress": ipAddress,
#         "connectionProfileUuid": connectionProfileUuid,
#         "cellId": cellId,
#         "importUuid": importUuid,
#         "mccMnc": mccMnc,
#         "imei": imei,
#         "planEntryUndefined": planEntryUndefined,
#     }

#     return document