from app import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)
    answer_text = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, question_text, answer_text):
        self.question_text = question_text
        self.answer_text = answer_text
