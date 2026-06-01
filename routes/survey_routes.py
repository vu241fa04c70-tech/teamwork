from flask import Blueprint, request, jsonify
from services.survey_service import add_survey

survey_bp = Blueprint('survey', __name__)

@survey_bp.route('/survey', methods=['POST'])
def survey():
    """
    Submit Survey
    ---
    tags:
      - Surveys

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

            target_market:
              type: string
              example: Students

            expected_users:
              type: integer
              example: 5000

            feedback_score:
              type: integer
              example: 9

    responses:
      200:
        description: Survey Submitted Successfully
    """
    return jsonify(add_survey(request.json))