import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator

from validator.validate import load_project, load_schema, validate_project


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "project.schema.json"


VALID_PROJECT = {
    "schema_version": "1.0",
    "id": "ml-001",
    "title": "Ordinary Least Squares Regression from Scratch",
    "domain": "Machine Learning",
    "topics": [
        "Linear Regression",
        "Ordinary Least Squares",
    ],
    "project_type": "algorithm_implementation",
    "difficulty": "beginner",
    "status": "completed",
    "technologies": [
        "Python",
        "NumPy",
    ],
    "capabilities": [
        "PREDICT",
        "EVALUATE",
    ],
}


def write_yaml(path: Path, data: dict) -> None:
    path.write_text(
        yaml.safe_dump(data, sort_keys=False),
        encoding="utf-8",
    )


def write_json(path: Path, data: dict) -> None:
    path.write_text(
        json.dumps(data),
        encoding="utf-8",
    )


def test_valid_yaml_project(tmp_path):
    project_path = tmp_path / "project.yaml"
    write_yaml(project_path, VALID_PROJECT)

    errors = validate_project(
        str(project_path),
        str(SCHEMA_PATH),
    )

    assert errors == []


def test_valid_json_project(tmp_path):
    project_path = tmp_path / "project.json"
    write_json(project_path, VALID_PROJECT)

    errors = validate_project(
        str(project_path),
        str(SCHEMA_PATH),
    )

    assert errors == []


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("id", "ML-001"),
        ("project_type", "invalid_type"),
        ("difficulty", "super_easy"),
        ("status", "unknown"),
    ],
)
def test_invalid_enum_or_pattern_values(tmp_path, field, value):
    project = VALID_PROJECT.copy()
    project[field] = value

    project_path = tmp_path / "project.yaml"
    write_yaml(project_path, project)

    errors = validate_project(
        str(project_path),
        str(SCHEMA_PATH),
    )

    assert errors


def test_invalid_capability(tmp_path):
    project = VALID_PROJECT.copy()
    project["capabilities"] = ["MAGIC"]

    project_path = tmp_path / "project.yaml"
    write_yaml(project_path, project)

    errors = validate_project(
        str(project_path),
        str(SCHEMA_PATH),
    )

    assert errors


def test_missing_required_field(tmp_path):
    project = VALID_PROJECT.copy()
    del project["title"]

    project_path = tmp_path / "project.yaml"
    write_yaml(project_path, project)

    errors = validate_project(
        str(project_path),
        str(SCHEMA_PATH),
    )

    assert errors


def test_empty_topics_rejected(tmp_path):
    project = VALID_PROJECT.copy()
    project["topics"] = []

    project_path = tmp_path / "project.yaml"
    write_yaml(project_path, project)

    errors = validate_project(
        str(project_path),
        str(SCHEMA_PATH),
    )

    assert errors


def test_malformed_yaml(tmp_path):
    project_path = tmp_path / "project.yaml"

    project_path.write_text(
        "id: ml-001\n"
        "title: [this is not valid YAML\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Invalid project document"):
        load_project(project_path)


def test_unsupported_file_type(tmp_path):
    project_path = tmp_path / "project.txt"
    project_path.write_text("hello", encoding="utf-8")

    with pytest.raises(
        ValueError,
        match="Unsupported project format",
    ):
        load_project(project_path)


def test_missing_project_file(tmp_path):
    project_path = tmp_path / "does-not-exist.yaml"

    with pytest.raises(ValueError, match="File not found"):
        load_project(project_path)


def test_schema_is_valid():
    schema = load_schema(SCHEMA_PATH)

    Draft202012Validator.check_schema(schema)