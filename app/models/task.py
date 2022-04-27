from db import db

class Task(db.Model):
    __tablename__ = 'tasks'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    status = db.Column(db.Boolean, index=True, unique=False)

    def __repr__(self):
        return '<Task {}>'.format(self.id) 
    
    def __init__(self, name, status=False):
        self.name = name
        self.status = status