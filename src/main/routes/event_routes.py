from flask import Blueprint, jsonify, request
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest
from src.data.event_handler import EventHandler

event_route_bp = Blueprint('event_route', __name__)

@event_route_bp.route('/events', methods=['POST'])
def create_event():
    http_request = HttpRequest(body=request.json)
    event_handler = EventHandler()

    response = event_handler.register(http_request)
    return jsonify(response.body), response.status_code