"""FastAPI application for the AI Project Atlas website."""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from importer.import_project import import_project
from catalogue.loader import (
    get_catalogue_project_metadata,
    load_catalogue,
    order_projects,
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]

SCHEMA_FILE = PROJECT_ROOT / "schemas" / "project.schema.json"
CATALOGUE_FILE = PROJECT_ROOT / "catalogue" / "catalogue.yaml"
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
    catalogue = load_catalogue(CATALOGUE_FILE)

    projects_directory = PROJECT_ROOT / "projects"

    for project_file in sorted(
        projects_directory.rglob("project.yaml")
    ):
        project = import_project(
            project_file,
            SCHEMA_FILE,
        )

        metadata = project.metadata.copy()

        catalogue_metadata = get_catalogue_project_metadata(
            metadata["id"],
            catalogue,
        )

        if catalogue_metadata is not None:
            metadata.update(catalogue_metadata)

        projects.append(metadata)

    return order_projects(projects, catalogue)


@app.get("/api/projects/{project_id}")
def get_project(project_id: str):
    """Return metadata for one Atlas project."""

    projects_directory = PROJECT_ROOT / "projects"

    project_file = next(
        projects_directory.rglob(
            f"{project_id}/project.yaml"
        ),
        None,
    )

    if project_file is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    project = import_project(
        project_file,
        SCHEMA_FILE,
    )

    metadata = project.metadata.copy()
    catalogue = load_catalogue(CATALOGUE_FILE)

    catalogue_metadata = get_catalogue_project_metadata(
        metadata["id"],
        catalogue,
    )

    if catalogue_metadata is not None:
        metadata.update(catalogue_metadata)

    return metadata


