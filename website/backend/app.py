"""FastAPI application for the AI Project Atlas website."""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from importer.import_project import import_project

PROJECT_ROOT = Path(__file__).resolve().parents[2]

SCHEMA_FILE = PROJECT_ROOT / "schemas" / "project.schema.json"

WEBSITE_DIRECTORY = PROJECT_ROOT / "website"


app = FastAPI(
    title="AI Project Atlas",
    description="Backend API for the AI Project Atlas MVP.",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-project-atlas.onrender.com",
    ],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


app.mount(
    "/website",
    StaticFiles(directory=WEBSITE_DIRECTORY, html=True),
    name="website",
)


@app.get("/")
def read_root():
    """Return a simple API health message."""
    return {
        "message": "AI Project Atlas API is running"
    }


@app.get("/api/projects")
def get_projects():
    """Return metadata for all Atlas projects."""

    projects = []

    projects_directory = PROJECT_ROOT / "projects"

    for project_directory in sorted(projects_directory.iterdir()):
        project_file = project_directory / "project.yaml"

        if not project_file.exists():
            continue

        project = import_project(
            project_file,
            SCHEMA_FILE,
        )

        projects.append(project.metadata)

    return projects


@app.get("/api/projects/{project_id}")
def get_project(project_id: str):
    """Return metadata for one Atlas project."""

    project_file = (
        PROJECT_ROOT
        / "projects"
        / project_id
        / "project.yaml"
    )

    if not project_file.exists():
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    project = import_project(
        project_file,
        SCHEMA_FILE,
    )

    return project.metadata


