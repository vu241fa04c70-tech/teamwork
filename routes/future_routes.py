from flask import Blueprint, request, jsonify

future_bp = Blueprint('future', __name__)

@future_bp.route('/idea-score', methods=['POST'])
def idea_score():

    data = request.json

    idea = data.get("idea", "")

    score = min(len(idea) * 2, 100)

    return jsonify({
        "idea": idea,
        "innovation_score": score,
        "status": "AI Evaluation Completed"
    })