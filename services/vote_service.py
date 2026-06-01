from models.vote_model import Vote
from config.database import db

def add_vote(data):

    vote = Vote(
        idea_id=data['idea_id'],
        upvotes=data['upvotes']
    )

    db.session.add(vote)
    db.session.commit()

    return {"message":"Vote Added"}