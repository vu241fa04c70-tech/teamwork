from flask import Blueprint, request, jsonify
from services.idea_service import add_idea, get_ideas
from middleware.jwt_middleware import token_required

idea_bp = Blueprint('idea', __name__)

@idea_bp.route('/idea', methods=['POST'])
@token_required
def create_idea():
    """
    Create Startup Idea
    ---
    tags:
      - Ideas

    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: JWT Token

      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: AI Study Buddy

            description:
              type: string
              example: AI powered learning assistant

            category:
              type: string
              example: Education

            founder:
              type: string
              example: Kanchana

    responses:
      200:
        description: Idea created successfully
    """
    return jsonify(add_idea(request.json))


@idea_bp.route('/ideas', methods=['GET'])
def all_ideas():
    """
    View All Ideas
    ---
    tags:
      - Ideas

    responses:
      200:
        description: List of all startup ideas
    """
    return jsonify(get_ideas())