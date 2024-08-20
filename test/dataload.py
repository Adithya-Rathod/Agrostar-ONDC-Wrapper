# from utils.db import MongoDBClient
# db = MongoDBClient()
import json
import uuid
import copy
import time
import requests


from datetime import datetime
# import pytz


# import pymongo
# from pymongo import MongoClient
# class MongoDBClient:
#     def __init__(self, uri="mongodb://localhost:27017", db_name="ONDC"):
#         self.client = MongoClient(uri)
#         self.db = self.client[db_name]
#         self.requestTable = self.db['requests']
        
#         try:
#             self.client.admin.command('ismaster')
#             print("MongoDB connection was succesful")
#         except ConnectionError as e:
#             print(f"MongoDB conncetion failed , {e}")
            
#     def insert_request(self, transactionID, context, message, status):
#         document = {
#             "id": transactionID,
#             "context": context,
#             "message": message,
#             "status" : "status",
#             "timestamp" : context.get("timestamp", ""),
#             "ttl" : context.get("ttl", ""),
#             "expiryTime": context.get("expiryTime", "")
#         }
#         return self.requestTable.insert_one(document)
    
#     def fetch_latest(self):
#         current_time = datetime.now(pytz.utc).isoformat()
#         return self.requestTable.find_one_and_update(
#             {"status": "received", "expiryTime": {"$gt": current_time}},
#             {"$set": {"status": "processing"}},
#             sort=[("timestamp", pymongo.ASCENDING)]
#         )
#     def find_expired(self):
#         current_time = datetime.now(pytz.utc).isoformat()
#         self.requestTable.update_many({"status": "received"})
#     def update_status(self, transactionID, status, tostatus):
#         return self.requestTable.update_one(
#             {"id": transactionID, "status": status},
#             {"$set": {"status": tostatus}})
    
#     def update_status_with_message(self, transactionID, status, tostatus, msg):
#         self.requestTable.update_one(
#             {"id": transactionID, "status": status},
#             {"$set": {"status": tostatus, "error-message": msg}})



# client = MongoDBClient()
url = "http://127.0.0.1:8000/search"

def genTrxnID():
    return str(uuid.uuid4())

    
with open("test/search_by_item.json", "r") as file:
    data = json.load(file)

arr = ["power", "bol", "rapigen", "glyclean", "1233", "sanchar", "biosense", "bhumika", "atraz", "florofix"]
# print(json.dumps(data))

for i, j in enumerate(arr):
    newD = copy.deepcopy(data)
    newD["context"]["transaction_id"] = genTrxnID()
    newD["message"]["intent"]["item"]["descriptor"]["name"] = j
    newD["context"]["timestamp"] = str(datetime.now().isoformat())
    newD["context"]["ttl"] = str("PT24H")
    # client.insert_request(newD["context"]["transaction_id"], newD.get("context", {}), newD.get("message", {}), "trial")
    # print(newD)
    # print(client.fetch_latest())
    response = requests.post(url=url, json=newD)
    print(response.json())
    time.sleep(1)
    