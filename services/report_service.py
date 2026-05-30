from models.report_model import Report
from config.database import db

def create_report(data):

    report = Report(
        idea_id=data['idea_id'],
        validation_status=data['validation_status'],
        market_analysis=data['market_analysis']
    )

    db.session.add(report)
    db.session.commit()

    return {"message":"Validation Report Created"}