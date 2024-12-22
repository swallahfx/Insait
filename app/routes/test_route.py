from flask import Blueprint, jsonify, request

from app.controllers.question_controller import QuestionController
from app.routes.template import welcome_template

question_bp = Blueprint("question_bp", __name__)


@question_bp.route("/")
def home():
    return welcome_template


@question_bp.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    question_text = data.get("question")

    if not question_text:
        return jsonify({"error": "Question is required"}), 400

    question_controller = QuestionController()
    question, answer = question_controller.ask_question(question_text)

    return jsonify({"question": question.question_text, "answer": answer}), 200
