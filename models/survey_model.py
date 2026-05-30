from config.database import db

class Survey(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    idea_id = db.Column(db.Integer)
    target_market = db.Column(db.String(200))
    expected_users = db.Column(db.Integer)
    feedback_score = db.Column(db.Integer)