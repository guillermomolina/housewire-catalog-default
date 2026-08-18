# housewire-catalog

HouseWire type catalogs, consolidated as one monorepo of independent Python
packages. Each catalog is a self-contained package with its own manifest,
types, and `housewire.catalog` entry point — install them individually or point
`HOUSEWIRE_CATALOGS_DIR` (or the `catalog_paths` config) at this directory to
discover all of them from the filesystem.

## Layout

| Directory | Package | Manifest id |
|---|---|---|
| `default/` | `housewire-catalog-default` | `housewire.default` |
| `sonoff/` | `housewire-catalog-sonoff` | `housewire.sonoff` |
| `wago/` | `housewire-catalog-wago` | `housewire.wago` |

## Install

```bash
pip install ./default ./sonoff ./wago
```

Each package declares the default catalog as a dependency and its catalog
manifest pins the required `housewire.default` version.

## Filesystem discovery

The program treats this directory as a catalog search root (Ansible-collections
style). From a HouseWire checkout that has this repo at `catalogs/housewire`,
the default search paths already include it; otherwise set:

```bash
export HOUSEWIRE_CATALOGS_DIR=/path/to/housewire-catalog
```

or add `catalog_paths: ["/path/to/housewire-catalog"]` to the user or project
HouseWire config.
