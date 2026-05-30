from models.idea_model import Idea
from models.vote_model import Vote
from models.discussion_model import Discussion

def dashboard_data():

    return {
        "total_ideas": Idea.query.count(),
        "total_votes": Vote.query.count(),
        "total_discussions": Discussion.query.count()
    }