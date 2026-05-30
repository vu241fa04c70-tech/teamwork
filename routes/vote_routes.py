from flask import Blueprint, request, jsonify
from services.vote_service import add_vote

vote_bp = Blueprint('vote', __name__)

@vote_bp.route('/vote', methods=['POST'])
def vote():
    return jsonify(add_vote(request.json))