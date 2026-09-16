import pytest
from importer.import_project import import_project


def test_import_project_reads_project_metadata():
    """The importer should read a project's YAML metadata."""

    project = import_project(
        "projects/ml-001/project.yaml",
        "schemas/project.schema.json",
    )

    assert project.metadata["id"] == "ml-001"
    assert project.metadata["title"] == "Ordinary Least Squares Regression from Scratch"
    assert project.metadata["domain"] == "Machine Learning"
    assert "Linear Regression" in project.metadata["topics"]
    assert "NumPy" in project.metadata["technologies"]
    assert "PREDICT" in project.metadata["capabilities"]
    assert project.source_file.name == "project.yaml"


def test_import_project_rejects_invalid_metadata(tmp_path):
    """The importer should reject a project that violates the Atlas schema."""

    invalid_project = tmp_path / "project.yaml"

    invalid_project.write_text(
        """
schema_version: "1.0"
id: "INVALID-ID"
title: "Invalid Project"
domain: "Machine Learning"
topics:
  - Testing
project_type: "machine_learning"
difficulty: "beginner"
status: "planned"
technologies:
  - Python
capabilities:
  - PREDICT
""",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Project validation failed"):
        import_project(
            invalid_project,
            "schemas/project.schema.json",
        )