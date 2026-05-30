from flask import Blueprint, request, jsonify
from services.survey_service import add_survey

survey_bp = Blueprint('survey', __name__)

@survey_bp.route('/survey', methods=['POST'])
def survey():
    return jsonify(add_survey(request.json))