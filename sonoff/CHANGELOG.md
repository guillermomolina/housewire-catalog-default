# Changelog

## [0.8.0] — 2026-08-18

### Changed

- **Physical representation kinds are PascalCase.**
  `representations.physical.kind` is now `Fixed` / `Modular` / `Dynamic`.

## [0.7.0] — 2026-08-17

### Changed

- Device types use the renamed catalog tier: `kind: DeviceType` (was
  `ElementType`). Product types still extend `housewire.default.Relay`.

## [0.6.0] — 2026-08-15

### Changed

- Relay models inherit the new ``Element`` tier through
  ``housewire.default.Relay`` (which now extends ``housewire.default.Element``),
  so the program classifies ``MiniZbd`` / ``ZbminiR2`` as electrical elements.

## [0.5.0] — 2026-08-12

### Changed

- Breaking: manifest declares ``schema: catalog`` (replaces ``catalog/v2``).
  No alias.

## [0.4.0] — 2026-08-11

### Changed

- Removed the intermediate Domotics catalog dependency. Sonoff relay models
  now inherit directly from the Default relay and declare their own electrical
  terminals.

## [0.3.0] — 2026-08-10

### Added

- Installable `housewire-catalog-sonoff` Python package with dependencies on
  the default catalog.

## [0.2.0] — 2026-08-09

### Changed

- Redrew the MINI-ZBD physical representation to match the real 41 × 43 mm enclosure and terminal layout.
- Redrew the ZBMINIR2 physical representation with its real enclosure and six-position terminal block.

## [0.1.0] — 2026-08-09

### Added

- Sonoff ZBMiniR2 and MINI-ZBD definitions with physical SVG representations.
