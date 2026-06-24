# SUEWS Hackathon — Practice Repo

This is a **practice repository** for the SUEWS Community Hackathon, run against the
real challenge dataset, [UMEP-dev/uda-city-hackathon](https://github.com/UMEP-dev/uda-city-hackathon),
which is public ahead of/at kickoff. This is a rehearsal of the pipeline and the
analysis approach, not a hackathon submission — the judged entry is a separate
repository created under the `UMEP-dev` organisation on the day.

## Pipeline smoke test

Before the real analysis, a minimal SUEWS run via [supy](https://supy.readthedocs.io/)
(the Python interface suews-agent wraps) confirmed the tooling works end to end, using
supy's own bundled sample dataset — see [`analysis/smoke_test.py`](../analysis/smoke_test.py)
and its [output](../analysis/smoke_test_output.txt).

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

## Results

**Dangerous-heat hours, present vs. +2.5 °C future** (full tables:
[present](../analysis/outputs/risk_present.csv), [future](../analysis/outputs/risk_future.csv)):

| Neighbourhood | Type | Hazard hrs (present) | Hazard hrs (future) | Risk rank (both) |
|---|---|---:|---:|---:|
| Kampong Lama | hotspot | 42 | 249 | **1** |
| Dhobi Lines | hotspot | 26 | 217 | 2–3 |
| Fuzhou Lanes | hotspot | 22 | 212 | 2–3 |
| Mlima Moto | hotspot | 5 | 149 | 4 |
| Lusitano Square | core | 5 | 129 | 5 |
| Victoria Exchange | core | 5 | 120 | 6 |
| Jade Gardens | refuge | **62** | **260** | 7 (tied last) |
| Taman Melati | refuge | 47 | 243 | 7 (tied last) |
| Serendib Rise | refuge | 26 | 205 | 7 (tied last) |
| Zheng He Towers | core | 2 | 77 | 7 (tied last) |

Two findings stand out:

1. **The hottest neighbourhoods are not the highest-risk ones.** The *refuge*
   neighbourhoods (Jade Gardens, Taman Melati) post the most dangerous-heat hours in
   both scenarios — low building roughness means weaker turbulent mixing and warmer
   near-surface air under NARP — but with zero exposed daytime population they rank
   **last** on risk. The dense informal *hotspot* neighbourhoods (Kampong Lama, Dhobi
   Lines, Fuzhou Lanes) have markedly fewer hazard hours yet rank **highest** risk,
   driven by exposure (300 people/ha) and vulnerability (low AC access, high outdoor
   work, high deprivation).
2. **Warming amplifies the hazard sharply but barely reshuffles the risk ranking.**
   Dangerous-heat hours rose 4–80× across neighbourhoods under +2.5 °C (e.g. Kampong
   Lama 42→249 hours), yet the risk-rank order is essentially unchanged — because
   exposure and vulnerability, not hazard, are what separate the top and bottom of the
   table here. That stability is itself informative: it suggests near-term adaptation
   priority (who needs protecting first) is robust to this warming scenario, even
   though the absolute hazard everyone faces is far higher.

## Where this bridge holds, and where it breaks

- **SUEWS gives an environmental hazard, not a health outcome.** `T2` over 35 °C is a
  proxy for dangerous conditions, not a prediction of heat-related illness or death.
- **35 °C dry-bulb is a debatable threshold for a humid city** (mean RH ≈ 81% here). A
  humid-heat index or wet-bulb/apparent-temperature metric would more honestly capture
  physiological danger; we used the dataset's illustrative default rather than
  re-deriving one, which is itself a limitation worth flagging.
- **The socio-economic layer is synthetic** — plausible magnitudes for a low-income
  tropical city, not survey data for a real place. Treat the *ranking* as the
  meaningful signal, not the absolute risk-index values.
- **Min–max scaling is relative to these ten neighbourhoods only** and does not
  transfer to other cities or datasets.
- **Neighbourhood-level aggregation hides intra-neighbourhood variation** — a
  district-mean vulnerability score can mask the most exposed individuals within it.
- **The future scenario is a uniform-delta pseudo-warming** (+2.5 K, RH-preserving),
  not a downscaled climate projection — a controlled "what if" stress test, not a
  forecast.
- **The geometric-mean combination is a deliberate choice**: a near-zero pillar (e.g.
  no exposed population) pulls risk to zero even under extreme hazard. An arithmetic
  mean would let one high pillar dominate instead — equally defensible, but not what
  we used here.

## Citing SUEWS

- Järvi, L., Grimmond, C.S.B. & Christen, A. (2011). The Surface Urban Energy and Water
  Balance Scheme (SUEWS): Evaluation in Los Angeles and Vancouver. *Journal of
  Hydrology*, 411(3–4), 219–237. https://doi.org/10.1016/j.jhydrol.2011.10.001
- Ward, H.C., Kotthaus, S., Järvi, L. & Grimmond, C.S.B. (2016). Surface Urban Energy and
  Water Balance Scheme (SUEWS): Development and evaluation at two UK sites. *Urban
  Climate*, 18, 1–32. https://doi.org/10.1016/j.uclim.2016.05.001
