import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


def load_project(path: Path) -> dict:
    """Load a project document from JSON or YAML."""

    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise ValueError(f"File not found: {path}")

    try:
        if path.suffix.lower() in {".yaml", ".yml"}:
            data = yaml.safe_load(text)
        elif path.suffix.lower() == ".json":
            data = json.loads(text)
        else:
            raise ValueError(
                "Unsupported project format. Use .json, .yaml, or .yml."
            )
    except (yaml.YAMLError, json.JSONDecodeError) as exc:
        raise ValueError(f"Invalid project document: {exc}")

    if not isinstance(data, dict):
        raise ValueError("Project document must contain an object/map.")

    return data


def load_schema(path: Path) -> dict:
    """Load the JSON Schema."""

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"Schema file not found: {path}")
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON Schema: {exc}")


def validate_project(project_path: str, schema_path: str) -> list[str]:
    """Validate a project document against the Atlas schema."""

    project = load_project(Path(project_path))
    schema = load_schema(Path(schema_path))

    validator = Draft202012Validator(schema)

    errors = sorted(
        validator.iter_errors(project),
        key=lambda error: list(error.path),
    )

    messages = []

    for error in errors:
        messages.append(f"{error.json_path}: {error.message}")

    return messages


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "Usage: python -m validator.validate "
            "<project.yaml|project.json> <schema.json>"
        )
        return 2

    project_path = sys.argv[1]
    schema_path = sys.argv[2]

    try:
        errors = validate_project(project_path, schema_path)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALIDATION PASSED")
    print(f"Project: {project_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())