import pymongo
from pymongo import MongoClient

from datetime import datetime
import pytz

class MongoDBClient:
    def __init__(self, uri="mongodb://localhost:27017", db_name="ONDC"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.requestTable = self.db['requests']
        
        try:
            self.client.admin.command('ismaster')
            print("MongoDB connection was succesful")
        except ConnectionError as e:
            print(f"MongoDB conncetion failed , {e}")
            
    def insert_request(self, transactionID, context, message, status):
        document = {
            "id": transactionID,
            "context": context,
            "message": message,
            "status" : status,
            "timestamp" : context.get("timestamp", ""),
            "ttl" : context.get("ttl", ""),
            "expiryTime": context.get("expiryTime", "")
        }
        return self.requestTable.insert_one(document)
            
    def fetch_latest(self):
        current_time = datetime.now().isoformat()
        return self.requestTable.find_one_and_update(
            {"status": "received", "expiryTime": {"$gt": current_time}},
            {"$set": {"status": "processing"}},
            sort=[("timestamp", pymongo.ASCENDING)]
        )
        
    def fetch(self):
        return self.requestTable.find({"status": "received"})
    def find_expired(self):
        current_time = datetime.now(pytz.utc).isoformat()
        self.requestTable.update_many({"status": "received", "expriryTime" : {"$let": current_time}}, 
                                      {"$set":{"status": "Expired"}})
    def update_status(self, transactionID, status, tostatus):
        return self.requestTable.update_one(
            {"id": transactionID, "status": status},
            {"$set": {"status": tostatus}})
    
    def update_status_with_message(self, transactionID, status, tostatus, msg):
        self.requestTable.update_one(
            {"id": transactionID, "status": status},
            {"$set": {"status": tostatus, "error-message": msg}})
        
client = MongoDBClient()
# client.insert_request("1234", {"lund": "puddi"}, {"gaand": "chudi"}, "received")
obj = list(client.fetch())
print(obj)