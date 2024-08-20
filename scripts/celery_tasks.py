from utils.db import MongoDBClient
from controller.callback_routes import on_search
from clients.agrostar_client import AgrostarAPIClient
from utils.expiry_time_calculator import calculate_expiry_time
from celery import Celery

capp = Celery('tasks', 
              broker='redis://localhost',
              backend='redis://localhost')
# capp.conf.timezone = 'UTC'

capp.conf.beat_schedule = {
    'process-search-request-every-10-seconds': {
        'task': 'process_search_request',
        'schedule': 10.0  # Every 5 seconds
    }
}

@capp.task
def enque_tasks(req):
            
    
    context = req.get("context", {})
    message = req.get("message", {})
    
    transactionID = context.get("transaction_id", "")
    ttl = context.get("ttl", "")
    timestamp = context.get("timestamp", "")
    expiryTime = calculate_expiry_time(timestamp, ttl)
    
    context.update({"expiryTime" : expiryTime})
    
    # inserting into the db (enqueue process)
    dbClient = MongoDBClient()
    stats= dbClient.insert_request(transactionID, context , message, "received")
    if stats is not None:
        print("succesfully recieved and stored request")
    else:
        print("failed to load the request")
        
@capp.task(name='process_search_request')
def process_search_request():

    dbclient = MongoDBClient()

    document = dbclient.fetch_latest()
    
    if document is not None:
        search_string = document.get("message", {}).get("intent", {}).get("item", {}).get("descriptor", {}).get("name", "")
        transactionID = document["id"]
        catalog  = AgrostarAPIClient.searchProducts(search_string)
        stat = on_search(catalog, document)
        
        if stat["message"]["ack"]["status"] == "ACK":
            MongoDBClient.update_status(transactionID, "processing", "completed")
            print("the document SUCCESSFULLY transformed !")
        else:
            error = stat["error"]
            MongoDBClient.update_status_with_message(transactionID, "processing", "failed", error)
            print("the document FAILED to transform!")
    else:
        print("The Document wasn't available in the DB..")
    

