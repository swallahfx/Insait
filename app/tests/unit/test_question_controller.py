from unittest.mock import patch

import pytest

from app.controllers.question_controller import QuestionController
from app.database.models import Question


@pytest.fixture
def mock_openai_answer():
    return "This is a mock answer from OpenAI."


@patch("app.controllers.question_controller.get_openai_answer")
def test_ask_question(mock_get_openai_answer, mock_openai_answer, app, db_session):
    """
    Test the QuestionController's ability to handle a question.
    """
    mock_get_openai_answer.return_value = mock_openai_answer

    with app.app_context():
        question, answer = QuestionController.ask_question("What is AI?")

    saved_question = (
        db_session.query(Question).filter_by(question_text="What is AI?").first()
    )
    assert saved_question is not None
    assert saved_question.answer_text == mock_openai_answer
    assert answer == mock_openai_answer
