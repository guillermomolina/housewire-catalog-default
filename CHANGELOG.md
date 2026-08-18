# Changelog

All notable changes to the **housewire-catalog** monorepo are documented here.
Each catalog package keeps its own changelog under its directory.

## [2026-08-18]

### Changed

- **Physical representation kinds are PascalCase** in all three catalogs
  (`default` 0.35.0, `sonoff` 0.8.0, `wago` 0.2.0): `representations.physical.kind`
  is now `Fixed` / `Modular` / `Dynamic`, matching the HouseWire model
  convention. Legacy lowercase kinds are rejected by current HouseWire.

## [2026-08-17]

### Changed

- Consolidated the default, Sonoff, and Wago catalogs into one monorepo with
  independent packages under `default/`, `sonoff/`, and `wago/`.
- Sonoff catalog id renamed `sonoff.devices` → `housewire.sonoff`.
