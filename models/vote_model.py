from config.database import db

class Vote(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    idea_id = db.Column(db.Integer)
    upvotes = db.Column(db.Integer)