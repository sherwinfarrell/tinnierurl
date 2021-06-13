from flask_sqlalchemy import SQLAlchemy
from app.db import db

class TinnieRepository(db.Model):
    __tablename__ = 'urltracker'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(500), unique=True)

    def __init__(self, url):
        self.url = url

def check_url(query_url):
    try:
        count = db.session.query(TinnieRepository).filter(TinnieRepository.url == query_url).count()
        return count != 0
    except Exception as e:
        raise Exception(f"Failed to verify the url in db becuase: {e}")

def return_id(url):
    try:
        row = db.session.query(TinnieRepository).filter(TinnieRepository.url == url).first()
        return row.id
    except Exception as e:
        raise Exception(f"Failed to get the id of the url because of: {e}")

def add_url(url):
    print(db)
    try:
        data = TinnieRepository(url)
        db.session.add(data)
        db.session.commit()
        return data.id
    except Exception as e:
        raise Exception(f"Adding of url to Db was Unsuccessful because {e}")

def get_url(id):
    row = db.session.query(TinnieRepository).filter(TinnieRepository.id == id)
    try: 
        url = row[0].url
        return url
    except Exception as e:
        return None
        
