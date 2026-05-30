from flask import Blueprint, request, jsonify
from services.report_service import create_report

report_bp = Blueprint('report', __name__)

@report_bp.route('/report', methods=['POST'])
def report():
    return jsonify(create_report(request.json))