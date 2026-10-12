"""Utilities for loading and ordering AI Project Atlas catalogue metadata."""

from pathlib import Path

import yaml


def load_catalogue(path: str | Path) -> dict:
    """Load the Atlas catalogue YAML file."""

    catalogue_path = Path(path)

    try:
        text = catalogue_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise ValueError(f"Catalogue file not found: {catalogue_path}")

    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        raise ValueError(f"Invalid catalogue document: {exc}")

    if not isinstance(data, dict):
        raise ValueError("Catalogue document must contain an object/map.")

    return data


def order_projects(projects: list[dict], catalogue: dict) -> list[dict]:
    """Return projects in Atlas-defined domain and project order."""

    domain_order = {
        domain["name"]: domain["display_order"]
        for domain in catalogue["domains"]
    }

    project_order = {}

    for domain in catalogue["domains"]:
        for project in domain["projects"]:
            project_order[project["id"]] = project["display_order"]

    return sorted(
        projects,
        key=lambda project: (
            domain_order.get(
                project["domain"],
                float("inf"),
            ),
            project_order.get(
                project["id"],
                float("inf"),
            ),
        ),
    )

def get_catalogue_project_metadata(
    project_id: str,
    catalogue: dict,
) -> dict | None:
    """Return Atlas-owned catalogue metadata for one project."""

    for domain in catalogue["domains"]:
        for project in domain["projects"]:
            if project["id"] == project_id:
                return {
                    "catalogue_reference": project["catalogue_reference"],
                    "domain_key": domain["key"],
                    "domain_code": domain["code"],
                }

    return None