from config.database import db

class Report(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    idea_id = db.Column(db.Integer)
    validation_status = db.Column(db.String(100))
    market_analysis = db.Column(db.Text)