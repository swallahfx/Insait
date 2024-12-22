from app import db
from app.database.models import Question
from app.integrations.openai import get_openai_answer


class QuestionController:

    @staticmethod
    def ask_question(question_text):
        # Get the answer from OpenAI
        answer_text = get_openai_answer(question_text)

        question = Question(question_text=question_text, answer_text=answer_text)
        db.session.add(question)
        db.session.commit()

        return question, answer_text
