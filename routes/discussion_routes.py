from flask import Blueprint, request, jsonify
from services.discussion_service import add_discussion

discussion_bp = Blueprint('discussion', __name__)

@discussion_bp.route('/discussion', methods=['POST'])
def discussion():
    """
    Add Discussion
    ---
    tags:
      - Discussions

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

            comment:
              type: string
              example: Great startup idea

            username:
              type: string
              example: Kanchana

    responses:
      200:
        description: Discussion Added Successfully
    """
    return jsonify(add_discussion(request.json))