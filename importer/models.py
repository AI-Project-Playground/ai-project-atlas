from dataclasses import dataclass
from pathlib import Path


@dataclass
class ImportedProject:
    """Internal Atlas representation of an imported project."""

    metadata: dict
    source_file: Path