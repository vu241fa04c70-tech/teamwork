from flask import Blueprint, jsonify
from services.dashboard_service import dashboard_data

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard', methods=['GET'])
def dashboard():
    """
    Dashboard Analytics
    ---
    tags:
      - Dashboard

    responses:
      200:
        description: Dashboard Statistics
    """
    return jsonify(dashboard_data())