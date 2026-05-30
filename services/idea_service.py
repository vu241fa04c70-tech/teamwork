from models.idea_model import Idea
from config.database import db

def add_idea(data):

    idea = Idea(
        title=data['title'],
        description=data['description'],
        category=data['category'],
        founder=data['founder']
    )

    db.session.add(idea)
    db.session.commit()

    return {"message":"Idea Posted Successfully"}

def get_ideas():

    ideas = Idea.query.all()

    result = []

    for i in ideas:

        result.append({
            "id":i.id,
            "title":i.title,
            "description":i.description,
            "category":i.category,
            "founder":i.founder
        })

    return result