"""Default HouseWire type catalog (installable package)."""

from __future__ import annotations

import os
import tempfile
from importlib import resources
from pathlib import Path

__version__ = "0.26.0"

_PKG = resources.files("housewire_catalog")


def _as_path(resource) -> Path | None:
    try:
        path = Path(os.fspath(resource))  # type: ignore[arg-type]
    except (TypeError, OSError, ValueError):
        return None
    return path if path.exists() else None


def catalog_root() -> Path:
    """Return a filesystem path to the catalog root (``catalog.yaml`` + ``types/``).

    Editable / extracted installs use the on-disk package directory. Zip wheels
    materialize under a temp cache.
    """
    # Prefer the package directory when it already holds catalog.yaml (src layout).
    direct = _as_path(_PKG)
    if direct is not None and (direct / "catalog.yaml").is_file():
        return direct.resolve()

    # Zip / missing real path: materialize catalog.yaml + types/.
    cache = Path(tempfile.gettempdir()) / "housewire-catalog-default" / __version__
    types_cache = cache / "types"
    if not (cache / "catalog.yaml").is_file():
        cache.mkdir(parents=True, exist_ok=True)
        types_cache.mkdir(parents=True, exist_ok=True)
        (cache / "catalog.yaml").write_bytes(
            _PKG.joinpath("catalog.yaml").read_bytes()
        )
        logo = _PKG.joinpath("logo.svg")
        if logo.is_file():
            (cache / "logo.svg").write_bytes(logo.read_bytes())
        for entry in _PKG.joinpath("types").iterdir():
            if entry.name.endswith((".yaml", ".yml")):
                (types_cache / entry.name).write_bytes(entry.read_bytes())
        symbols = _PKG.joinpath("types", "symbols")
        if symbols.is_dir():
            symbols_cache = types_cache / "symbols"
            symbols_cache.mkdir(parents=True, exist_ok=True)
            for entry in symbols.iterdir():
                if entry.name.endswith(".svg"):
                    (symbols_cache / entry.name).write_bytes(entry.read_bytes())
    return cache.resolve()


def types_dir() -> Path:
    """Return the directory of type YAML files."""
    path = catalog_root() / "types"
    if not path.is_dir():
        raise FileNotFoundError(f"Catalog types directory missing: {path}")
    return path


def catalog_id() -> str:
    """Return the catalog id from ``catalog.yaml`` (fallback ``default``)."""
    import yaml

    meta = catalog_root() / "catalog.yaml"
    try:
        data = yaml.safe_load(meta.read_text(encoding="utf-8")) or {}
    except OSError:
        return "default"
    if isinstance(data, dict) and data.get("id"):
        return str(data["id"])
    return "default"
