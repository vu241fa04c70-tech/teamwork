from config.database import db

class Collaboration(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    idea_id = db.Column(db.Integer)
    member_name = db.Column(db.String(100))
    role = db.Column(db.String(100))