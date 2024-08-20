from flask import Blueprint, request, jsonify
from utils.db import MongoDBClient
from clients.agrostar_client import AgrostarAPIClient
from scripts.celery_tasks import enque_tasks

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return "This is home"

@routes.route('/search', methods=['POST'])
def ingress():
    req = request.get_json()
    context = req.get("context", {})
    message = req.get("message", {})
    
    if not context or not message:
        return jsonify({"error": {"type" : "BAD REQUEST", "code" : "30000", "path":"/search", "message": "context or message absent"}})

    #trigger a background process as celery worker function
    enque_tasks.delay(req)

    # acknowledgement to the requested entity. 
    return jsonify(
        {
            "message": {
                "ack": {
                "status": "ACK"
                }
        }})

    

    