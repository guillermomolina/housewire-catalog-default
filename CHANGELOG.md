# Changelog

All notable changes to **housewire-catalog** are documented in this file.

Format inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/) and is
**independent** of the HouseWire program version.

Catalog metadata lives in `catalog.yaml` (`version:`).

## [Unreleased]

## [0.18.0] — 2026-08-09

### Added

- Physical SVG representations with routing-aligned terminal anchors for
  terminal strips, switches, sockets, relays, luminaires, protection devices,
  power supplies, intercoms, supplies, and earth electrodes.

### Removed

- The redundant ``PETerminal`` type; use a single-pole ``TerminalStrip`` with
  a PE-labelled terminal instead.

## [0.17.0] — 2026-08-05

### Added

- ``DeviceBox`` defaults: ``opening_grid`` ``NS: 1``, ``WE: 1``, ``B: 1``.

## [0.16.0] — 2026-08-05

### Added

- ``JunctionBox`` defaults: ``opening_grid`` ``NS: 2``, ``WE: 2``, ``B: 2x2``
  (applied when creating a new junction box).

## [0.15.0] — 2026-08-04

### Changed

- Enum values PascalCase: ``kind``, ``direction``, ``role``, and subtype
  ``install``/``mount`` defaults (``Flush``, ``Surface``, ``Wall``, …).

## [0.14.1] — 2026-08-04

### Changed

- ``Stair`` description no longer mentions removed ``connects`` field.

## [0.14.0] — 2026-08-04

### Changed

- Catalog type files use ``type:`` instead of ``id:``.
- Subtype keys are PascalCase (``IP40`` / ``IP65``, ``OneGang``, ``Tube``,
  ``Power``, ``Earth``, ``DC``, ``ZbminiR2``, …).

## [0.13.0] — 2026-08-04

### Added

- Closed ``subtypes`` maps: ``JunctionBox`` ``ip40`` / ``ip65`` (with
  ``install`` defaults flush / surface), ``DeviceBox`` gang sizes,
  ``LightPoint`` hole / emergency, ``Socket`` ``Schuko``.
- ``label_es`` on ``Conduit``, ``Cable``, ``Conductor``, ``Switch``, and
  ``Relay`` subtypes; default subtypes for Conduit (``tube``) and
  Cable/Conductor (``power``).

## [0.12.1] — 2026-08-04

### Changed

- ``JunctionBox`` Spanish label/description: «Caja de derivación» (was
  «Caja de empalme»).

## [0.12.0] — 2026-08-04

### Added

- Optional ``description_es`` on catalog metadata and all bundled types for
  Spanish UI descriptions (English ``description`` remains the default).

## [0.11.0] — 2026-08-04

### Added

- Optional ``label_es`` on catalog metadata and all bundled types for
  Spanish UI labels (English ``label`` remains the default).

## [0.10.0] — 2026-08-03

### Changed

- License switched from MIT to **Server Side Public License v1 (SSPL-1.0)**
  (see ``LICENSE``).

## [0.9.0] — 2026-08-03

### Changed

- Type ``icon:`` values are Lucide ids (``plug``, ``zap``, ``house``, …).

## [0.8.0] — 2026-08-02

### Added

- Installable Python package ``housewire-catalog`` with
  ``catalog_root()`` / ``types_dir()`` / ``catalog_id()``.
- ``pyproject.toml``; type YAML lives under ``src/housewire_catalog/``.
- Root ``catalog.yaml`` / ``types`` / ``logo.svg`` symlinks for clone-as-path
  compatibility.

## [0.7.0] — 2026-08-02

### Changed

- Type field ``description_es`` replaced by English ``description``.
- Spanish comments and mixed Spanish subtype labels removed from type YAML.

## [0.6.0] — 2026-08-02

### Changed

- Catalog display field ``title`` renamed to ``label`` (``name`` also
  accepted when reading). Type ``id`` stays the machine key.

## [0.5.0] — 2026-08-02

### Changed

- Terminal **ids** are face-cell tokens (``N1``, ``S2``, …); ``label`` holds
  casing marks (``L``, ``PE``, ``1``, …). Removed ``terminal_pairs``.
- TerminalStrip pins are ``N1``…``Nn`` (N-side convention) with ``NS`` grid.

## [0.4.0] — 2026-08-02

### Added

- ``Conductor`` type (``kind: conductor_type``) for leaf wires in house/v2
  ``cables:`` maps.

### Changed

- ``Cable`` is a sheath/bundle (``contains``); description updated for house/v2.
- ``Conduit`` description points at the unified ``cables:`` map.
- Catalog description targets house/v2 sites.

## [0.3.2] — 2026-08-02

### Changed

- Catalog title uses the **HouseWire** program name.

## [0.2.1] — 2026-08-01

### Added

- ``terminal_grid`` on Socket, Luminaire, Intercom, EarthElectrode,
  PowerSupply, and Relay (incl. ``mini_zbd`` subtype).

## [0.2.0] — 2026-08-01

### Added

- Element ``terminal_grid`` on MCB, MCB2P, RCD, TerminalStrip, Switch,
  Supply, and PETerminal (same face grammar as location ``opening_grid``).

## [0.1.0] — 2026-08-01

### Added

- Initial `catalog/v1` library: `catalog.yaml` + `types/*.yaml` (places,
  elements, cables, conduits) migrated out of the housewire package.
