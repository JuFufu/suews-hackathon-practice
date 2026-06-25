---
title: Method & Data
---

**[Home](index.html) · [Method & Data](method.html) · [Results & Drivers](results.html) · [Caveats](caveats.html) · [Risk Reduction](risk-reduction.html)**

---

## The question

Across UDA-city's ten neighbourhoods, **is the hottest place also the highest-risk
place?** We ran SUEWS for the present hot-humid season and a +2.5 °C hotter-future
pseudo-warming, derived a dangerous-heat-hours hazard layer, and bridged it to a
socio-economic heat-risk indicator using the dataset's reference bridge
(`risk_bridge.py`), following a UNDRR-style decomposition:

```
risk = (hazard × exposure × vulnerability) ^ (1/3)
```

each pillar min–max scaled to `[0, 1]` across the ten neighbourhoods. Hazard is
dangerous-heat hours (hourly-mean 2 m air temperature, `T2`, above 35 °C, illustrative
threshold, after a 14-day spin-up discard). Exposure is daytime population density.
Vulnerability combines five proxies: elderly/under-5 share, lack of AC access, outdoor
workers, and a deprivation index.

## Method

- **Model**: SUEWS v2026.6.5 (via supy), canonical config `uda-city.yml` — NARP net
  radiation + classic OHM storage heat, 10 grids run in parallel.
- **Forcing**: ERA5-derived hourly point series for a coastal, hot-humid setting
  (2024-03-02 to 2024-06-01 local; March is spin-up, the April–May window is analysed).
- **Scenarios**: *present* (direct ERA5) and *future* (+2.5 K uniform pseudo-warming,
  RH held constant, longwave-down scaled for grey-body consistency).
- **Anthropogenic heat is off** in both scenarios; population density feeds exposure and
  vulnerability, not the model's heat input.

Next: **[Results & Drivers](results.html)**
