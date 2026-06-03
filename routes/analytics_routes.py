from flask import Blueprint, jsonify
from models.idea_model import Idea
from models.vote_model import Vote
from models.discussion_model import Discussion

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route("/stats", methods=["GET"])
def analytics():

    total_ideas = Idea.query.count()
    total_votes = Vote.query.count()
    total_discussions = Discussion.query.count()

    return jsonify({
        "total_ideas": total_ideas,
        "total_votes": total_votes,
        "total_discussions": total_discussions
    })