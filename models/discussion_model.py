from config.database import db

class Discussion(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    idea_id = db.Column(db.Integer)
    comment = db.Column(db.Text)
    