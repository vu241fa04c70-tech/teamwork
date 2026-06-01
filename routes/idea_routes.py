from flask import Blueprint, request, jsonify
from services.idea_service import add_idea, get_ideas
from middleware.jwt_middleware import token_required

idea_bp = Blueprint('idea', __name__)

@idea_bp.route('/idea', methods=['POST'])
@token_required
def create_idea():
    """
    Create a startup idea
    ---
    tags:
      - Ideas
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Idea created successfully
    """
    return jsonify(add_idea(request.json))


@idea_bp.route('/ideas', methods=['GET'])
def all_ideas():
    return jsonify(get_ideas())