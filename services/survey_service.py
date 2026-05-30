from models.survey_model import Survey
from config.database import db

def add_survey(data):

    survey = Survey(
        idea_id=data['idea_id'],
        target_market=data['target_market'],
        expected_users=data['expected_users'],
        feedback_score=data['feedback_score']
    )

    db.session.add(survey)
    db.session.commit()

    return {"message":"Survey Submitted"}