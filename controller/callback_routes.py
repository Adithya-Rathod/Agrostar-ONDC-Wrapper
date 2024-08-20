from service.transformService import transform_search_request
import requests
import json
from utils.db import MongoDBClient

def on_search(catalog, req):
    
    transformedData = transform_search_request(catalog, req)
    
    url = req.get("context",  {}).get("bap_uri", "")
    url= url + "/on_search"
    # webhook to the URL and receive the response. 
    response = requests.post(url=url, json=json.dumps(transformedData))
    
    return response.json()
        