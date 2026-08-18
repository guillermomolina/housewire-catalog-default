"""Installed resource access for the HouseWire Wago catalog."""

from __future__ import annotations

from importlib import resources
from pathlib import Path


def catalog_root() -> Path:
    """Return the installed catalog root containing its manifest and types."""
    return Path(str(resources.files(__package__))).resolve()
