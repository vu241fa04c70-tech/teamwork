from flask import Flask
from flasgger import Swagger
from config.database import db

from routes.auth_routes import auth_bp
from routes.idea_routes import idea_bp
from routes.vote_routes import vote_bp
from routes.discussion_routes import discussion_bp
from routes.survey_routes import survey_bp
from routes.report_routes import report_bp
from routes.dashboard_routes import dashboard_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///startup_validation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secretkey'

db.init_app(app)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Startup Idea Validation Platform API",
        "description": "Collaborative Research APIs",
        "version": "1.0"
    },

    "tags": [
        {
            "name": "Authentication",
            "description": "User Registration and Login"
        },
        {
            "name": "Ideas",
            "description": "Startup Idea Management"
        },
        {
            "name": "Votes",
            "description": "Idea Voting"
        },
        {
            "name": "Discussions",
            "description": "Community Discussions"
        },
        {
            "name": "Surveys",
            "description": "Market Validation Surveys"
        },
        {
            "name": "Reports",
            "description": "Validation Reports"
        },
        {
            "name": "Dashboard",
            "description": "Analytics Dashboard"
        }
    ]
}
Swagger(app, template=swagger_template)

app.register_blueprint(auth_bp)
app.register_blueprint(idea_bp)
app.register_blueprint(vote_bp)
app.register_blueprint(discussion_bp)
app.register_blueprint(survey_bp)
app.register_blueprint(report_bp)
app.register_blueprint(dashboard_bp)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return {
        "message": "Collaborative Startup Idea Validation Platform"
    }

if __name__ == '__main__':
    app.run(debug=True)