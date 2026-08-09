<p align="center">
  <img src="src/housewire_catalog/logo.svg" alt="HouseWire" width="96" height="96">
</p>

# HouseWire catalog

External type catalog for [HouseWire](https://github.com/guillermomolina/housewire)
(`schema: catalog/v1`), installable as the Python package **`housewire-catalog-default`**.

Place types inherit behavior from abstract catalog bases. ``Container``
provides child containment without physical openings; ``ConnectablePlace``
adds optional ``opening_grid`` / ``openings`` support. Concrete semantic types
such as ``Room`` and ``JunctionBox`` extend one of these bases and remain the
types used in site YAML.

## Install

```bash
pip install housewire-catalog-default
# from a checkout:
pip install -e .
```

```python
from housewire_catalog import catalog_root, types_dir, catalog_id

print(catalog_root())  # …/catalog.yaml + types/
print(types_dir())
print(catalog_id())    # "default"
```

HouseWire resolves this package automatically when no `HOUSEWIRE_CATALOG` /
`catalogs/default` override is set (`pip install 'housewire[catalog]'`).

## Layout

```text
src/housewire_catalog/
  catalog.yaml     # id, version, label (catalog/v1)
  types/           # one YAML file per type
  logo.svg
pyproject.toml
CHANGELOG.md
```

Root `catalog.yaml` / `types/` / `logo.svg` are symlinks into
`src/housewire_catalog/` so a plain git clone still works as a catalog root.

Current catalog version: see `version:` in `catalog.yaml`.

## License

**Server Side Public License v1 (SSPL-1.0)** — see [LICENSE](LICENSE).
Copyright (c) 2026 Guillermo Adrián Molina.

Same terms as the HouseWire program: self-hosting and modification are fine;
offering the catalog (or a modified version) to third parties **as a service**
triggers the SSPL Service Source Code obligations.

## Use with HouseWire (path override)

```bash
mkdir -p catalogs
git clone https://github.com/guillermomolina/housewire-catalog-default.git catalogs/default
# catalogs/default (via symlinks) is a valid catalog root
export HOUSEWIRE_CATALOG=/path/to/housewire-catalog-default   # or catalogs/default
```

Site overlay: `$SITE/catalog/*.yaml` (shallow merge by `id`).
