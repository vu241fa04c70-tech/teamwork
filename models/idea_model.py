from config.database import db

class Idea(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    category = db.Column(db.String(100))
    founder = db.Column(db.String(100))