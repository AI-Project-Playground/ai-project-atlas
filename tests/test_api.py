"""Tests for the AI Project Atlas API."""

from fastapi.testclient import TestClient

from website.backend.app import app


client = TestClient(app)


def test_get_projects_returns_catalogue_metadata():
    """The projects endpoint should include Atlas-owned catalogue metadata."""

    response = client.get("/api/projects")

    assert response.status_code == 200

    projects = response.json()

    ml_project = next(
        project
        for project in projects
        if project["id"] == "ml-001"
    )

    assert ml_project["catalogue_reference"] == "ML-001"
    assert ml_project["domain_key"] == "machine-learning"
    assert ml_project["domain_code"] == "ML"


def test_get_project_returns_catalogue_metadata():
    """The project detail endpoint should include Atlas-owned metadata."""

    response = client.get("/api/projects/ml-001")

    assert response.status_code == 200

    project = response.json()

    assert project["id"] == "ml-001"
    assert project["catalogue_reference"] == "ML-001"
    assert project["domain_key"] == "machine-learning"
    assert project["domain_code"] == "ML"