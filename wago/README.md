# housewire-catalog-wago

Wago connection products (terminal strips, splices) as HouseWire catalog types.

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
