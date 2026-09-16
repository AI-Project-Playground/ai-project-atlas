"""Utilities for importing AI Project Atlas project metadata."""

import argparse
from pathlib import Path

import yaml

from importer.models import ImportedProject
from validator.validate import validate_project




def import_project(
    project_file: str | Path,
    schema_file: str | Path,
) -> ImportedProject:
    """Read a project.yaml file and return its structured metadata."""

    validation_errors = validate_project(
        str(project_file),
        str(schema_file),
    )

    if validation_errors:
        raise ValueError(
            "Project validation failed:\n"
            + "\n".join(validation_errors)
        )

    project_path = Path(project_file)

    with project_path.open("r", encoding="utf-8") as file:
        project_data = yaml.safe_load(file)

    return ImportedProject(
        metadata=project_data,
        source_file=project_path,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Import an AI Project Atlas project."
    )

    parser.add_argument(
        "project_file",
        help="Path to the project YAML or JSON file.",
    )

    parser.add_argument(
        "schema_file",
        help="Path to the Atlas project schema.",
    )

    args = parser.parse_args()

    project = import_project(
        args.project_file,
        args.schema_file,
    )

    print(f"Imported project: {project.metadata['id']}")
    print(f"Title: {project.metadata['title']}")