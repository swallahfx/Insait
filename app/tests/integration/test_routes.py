from unittest.mock import patch

import pytest


@pytest.fixture
def test_question_payload():
    return {"question": "What is the capital of France?"}


@patch("app.integrations.openai.get_openai_answer")
def test_ask_question_endpoint(mock_get_openai_answer, client, test_question_payload):
    """
    Test the `/ask` endpoint with mocked OpenAI API response.
    """
    mock_get_openai_answer.return_value = "The capital of France is Paris."

    response = client.post("/ask", json=test_question_payload)

    assert response.status_code == 200
    response_data = response.get_json()
    assert "question" in response_data
    assert "answer" in response_data
    assert response_data["answer"] == "The capital of France is Paris."
