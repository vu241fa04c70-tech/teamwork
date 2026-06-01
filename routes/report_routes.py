from flask import Blueprint, request, jsonify
from services.report_service import create_report

report_bp = Blueprint('report', __name__)

@report_bp.route('/report', methods=['POST'])
def report():
    """
    Generate Validation Report
    ---
    tags:
      - Reports

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

            validation_status:
              type: string
              example: Approved

            market_analysis:
              type: string
              example: High demand among students

    responses:
      200:
        description: Validation Report Generated Successfully
    """
    return jsonify(create_report(request.json))