from models.discussion_model import Discussion
from config.database import db

def add_discussion(data):

    discussion = Discussion(
        idea_id=data['idea_id'],
        comment=data['comment'],
        username=data['username']
    )

    db.session.add(discussion)
    db.session.commit()

    return {"message":"Discussion Added"}