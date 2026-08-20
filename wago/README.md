# housewire-catalog-wago

Wago connection products (terminal strips, splices) as HouseWire catalog types.

- Series 281 through terminal strips (`housewire.wago.TerminalStrip`):
  models 281-601 through 281-606 (1- to 6-pole).
- Series 221 lever-nut splicing connectors (`housewire.wago.SpliceConnector`):
  models 221-412 (2-way), 221-413 (3-way), and 221-415 (5-way), 4 mm².

- Library id: `housewire.wago`
- Maintained alongside the default and Sonoff catalogs in the
  `housewire-catalog` monorepo.
- Requires `housewire-catalog-default >= 0.34.0`.

Install from the monorepo:

```bash
pip install ./catalogs/housewire/wago
```

or reference it in a site document:

```yaml
catalogs:
  - housewire.default
  - housewire.wago
```

The program discovers an installed catalog through the `housewire.catalog`
entry-point group using its manifest id, `housewire.wago`.
