from flask import Blueprint, request, jsonify
from services.idea_service import add_idea, get_ideas
from middleware.jwt_middleware import token_required

idea_bp = Blueprint('idea', __name__)

@idea_bp.route('/idea', methods=['POST'])
@token_required
def create_idea():
    return jsonify(add_idea(request.json))

@idea_bp.route('/ideas', methods=['GET'])
def all_ideas():
    return jsonify(get_ideas())