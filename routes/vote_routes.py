from flask import Blueprint, request, jsonify
from services.vote_service import add_vote

vote_bp = Blueprint('vote', __name__)

@vote_bp.route('/vote', methods=['POST'])
def vote():
    """
    Vote for Idea
    ---
    tags:
      - Votes

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
            idea_id:
              type: integer
              example: 1

            upvotes:
              type: integer
              example: 1

    responses:
      200:
        description: Vote Added Successfully
    """
    return jsonify(add_vote(request.json))