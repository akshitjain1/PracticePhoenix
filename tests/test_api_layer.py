import pytest
from fastapi.testclient import TestClient
from app.api.main import app


client = TestClient(app)


def test_api_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "database" in data


def test_api_session_today_endpoint():
    response = client.get("/session/today")
    assert response.status_code == 200
    data = response.json()
    assert "welcome_dashboard" in data
    assert "news_section" in data


def test_api_revision_endpoint():
    response = client.get("/revision")
    assert response.status_code == 200
    data = response.json()
    assert "total_pending" in data
    assert isinstance(data["categories"], list)


def test_api_progress_endpoint():
    response = client.get("/progress")
    assert response.status_code == 200
    data = response.json()
    assert "overall_percentage" in data
    assert "categories" in data


def test_api_history_endpoint():
    response = client.get("/history?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert "total_returned" in data
    assert isinstance(data["briefs"], list)


def test_api_analytics_endpoint():
    response = client.get("/analytics")
    assert response.status_code == 200
    data = response.json()
    assert "total_interactions" in data
    assert isinstance(data["weakness_rankings"], list)


def test_api_roadmap_endpoint():
    response = client.get("/roadmap")
    assert response.status_code == 200
    data = response.json()
    assert "total_remaining_lessons" in data
    assert "estimated_days_to_complete" in data


def test_api_interview_workflow_endpoints():
    q_res = client.get("/interview/question?user_id=api_test_user&category=operating_systems")
    assert q_res.status_code == 200
    q_data = q_res.json()
    assert "session_id" in q_data
    assert "question_text" in q_data

    ans_payload = {
        "user_id": "api_test_user",
        "answer_text": "Virtual memory uses page tables and TLB to map virtual addresses to physical memory frames."
    }
    ans_res = client.post("/interview/answer", json=ans_payload)
    assert ans_res.status_code == 200
    ans_data = ans_res.json()
    assert "evaluation_report_md" in ans_data
    assert "overall_score" in ans_data
    assert ans_data["overall_score"] > 0
