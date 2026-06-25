---
title: Caveats
---

**[Home](index.html) · [Method & Data](method.html) · [Results & Drivers](results.html) · [Caveats](caveats.html) · [Risk Reduction](risk-reduction.html)**

---

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
- **The "hotspot" label doesn't match its implied building form.** Classifying each
  neighbourhood's Local Climate Zone (Stewart & Oke, 2012) from `λp` and mean building
  height, the four `hotspot` neighbourhoods — described as "dense informal
  settlements" — have footprints of only 0.14–0.35, well below the 0.6–0.9 that LCZ 7
  (lightweight low-rise, the standard informal-settlement signature) would require.
  Their nearest LCZ is actually 9 (sparsely built) or the LCZ 6/8 boundary. The heat/risk
  signal we found for these neighbourhoods comes from who lives there (exposure,
  vulnerability), not from informal-settlement-style building density — worth being
  precise about so the result isn't misread as a building-morphology finding.
- **No wind direction, and a direction-blind model** (see [Results & Drivers](results.html)) —
  real ventilation differences between neighbourhoods of identical bulk roughness are
  invisible here.

Next: **[Risk Reduction](risk-reduction.html)**
