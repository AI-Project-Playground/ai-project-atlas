import pytest

from catalogue.loader import (
    get_catalogue_project_metadata,
    load_catalogue,
    order_projects,
)


def test_load_catalogue_reads_catalogue_metadata():
    """The catalogue loader should read Atlas catalogue metadata."""

    catalogue = load_catalogue("catalogue/catalogue.yaml")

    assert "domains" in catalogue
    assert catalogue["domains"][0]["key"] == "mathematical-foundations"
    assert catalogue["domains"][0]["display_order"] == 1

    machine_learning = next(
        domain
        for domain in catalogue["domains"]
        if domain["key"] == "machine-learning"
    )

    assert machine_learning["display_order"] == 3
    assert machine_learning["projects"][0]["id"] == "ml-001"
    assert machine_learning["projects"][1]["id"] == "ml-002"


def test_load_catalogue_rejects_invalid_document(tmp_path):
    """The catalogue loader should reject a non-map YAML document."""

    invalid_catalogue = tmp_path / "catalogue.yaml"

    invalid_catalogue.write_text(
        """
- invalid
- catalogue
""",
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="Catalogue document must contain an object/map",
    ):
        load_catalogue(invalid_catalogue)


def test_order_projects_follows_catalogue_order():
    """Projects should be ordered using Atlas catalogue metadata."""

    catalogue = load_catalogue("catalogue/catalogue.yaml")

    projects = [
        {
            "id": "ml-002",
            "domain": "Machine Learning",
        },
        {
            "id": "dl-001",
            "domain": "Deep Learning",
        },
        {
            "id": "ml-001",
            "domain": "Machine Learning",
        },
        {
            "id": "genai-001",
            "domain": "Generative AI",
        },
    ]

    ordered = order_projects(projects, catalogue)

    assert [project["id"] for project in ordered] == [
        "ml-001",
        "ml-002",
        "dl-001",
        "genai-001",
    ]


def test_catalogue_references_are_unique():
    """Every project should have a unique permanent catalogue reference."""

    catalogue = load_catalogue("catalogue/catalogue.yaml")

    references = [
        project["catalogue_reference"]
        for domain in catalogue["domains"]
        for project in domain["projects"]
    ]

    assert len(references) == len(set(references))


def test_get_catalogue_project_metadata():
    """The helper should return Atlas-owned metadata for a project."""

    catalogue = load_catalogue("catalogue/catalogue.yaml")

    metadata = get_catalogue_project_metadata("ml-001", catalogue)

    assert metadata == {
        "catalogue_reference": "ML-001",
        "domain_key": "machine-learning",
        "domain_code": "ML",
    }