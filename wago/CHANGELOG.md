# Changelog

All notable changes to **housewire-catalog-wago** are documented in this file.

Format inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

## [0.3.0] — 2026-08-20

### Added

- **Wago 221 lever-nut splicing connectors** (`housewire.wago.SpliceConnector`)
  with dedicated SVGs. Series 221 compact splices (4 mm²) as a series type
  with one subtype per model: 221-412 (2-way), 221-413 (3-way), and 221-415
  (5-way). Single-pole device: every lever slot clamps one conductor and all
  share the same potential; terminals land on the N face (`N1..Nn`).

## [0.2.0] — 2026-08-18

### Changed

- **Physical representation kinds are PascalCase.**
  `representations.physical.kind` is now `Fixed` / `Modular` / `Dynamic`.

## [0.1.0] — 2026-08-17

### Added

- Initial Wago catalog (`housewire.wago`) with a 3-pole through terminal strip
  (`housewire.wago.TerminalStrip`, series 281).
