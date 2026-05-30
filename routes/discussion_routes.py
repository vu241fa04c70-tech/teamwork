from flask import Blueprint, request, jsonify
from services.discussion_service import add_discussion

discussion_bp = Blueprint('discussion', __name__)

@discussion_bp.route('/discussion', methods=['POST'])
def discussion():
    return jsonify(add_discussion(request.json))