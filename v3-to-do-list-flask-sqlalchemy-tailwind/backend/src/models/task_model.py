from db.db_connection import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return self.text
    
    def to_dict(self):
        return {"id": self.id, "text": self.text, "done": self.done}