# Real-analysis session transcript — 2026-06-24

AI agent: Claude Code (Sonnet 4.6). Follow-on to the initial setup session
([`2026-06-24-setup-session.md`](2026-06-24-setup-session.md)): pulling in the actual
UDA-city challenge dataset and running the real heat-hazard + risk-bridge analysis,
rather than just the supy sample-data smoke test.

## What was asked

> Pull this in now and start the real analysis.

(referring to https://github.com/UMEP-dev/uda-city-hackathon, the focus-city dataset
for the SUEWS Community Hackathon)

## Steps taken

1. **Pulled the dataset.** Cloned `UMEP-dev/uda-city-hackathon` into `data/`, then
   removed its embedded `.git` directory so the files are tracked as plain content in
   this practice repo (avoids an unintended nested-repo/gitlink). Read
   `agent_manifest.yml` first, as instructed by the dataset's own README — it points at
   the canonical config (`uda-city.yml`, 10 neighbourhoods), the two scenarios
   (`scenarios.yml`), and the reference risk bridge (`risk_bridge.py` / `risk_bridge.md`).
2. **Ran the present scenario.**
   ```
   python risk_bridge.py --out outputs/derived/risk_present.csv
   ```
   This runs SUEWS live (10 grids in parallel via supy's Rust/Rayon backend) on the
   canonical config's default forcing (`forcing/present_hot_humid/UDA_2024_data_60.txt`),
   computes dangerous-heat hours (hourly-mean `T2` > 35°C, after a 14-day spin-up
   discard), and joins it with exposure (daytime population density) and vulnerability
   (five socio-economic proxies) to produce a ranked risk table.
3. **Ran the future scenario.**
   ```
   python risk_bridge.py --forcing forcing/future_hot_humid/UDA_2024_data_60.txt --out outputs/derived/risk_future.csv
   ```
   Same pipeline, +2.5°C RH-preserving pseudo-warming forcing.
4. **Compared results.** Both output tables were copied into
   [`analysis/outputs/`](../analysis/outputs/) (`risk_present.csv`, `risk_future.csv`).

## Result

| Neighbourhood | Type | Hazard hrs (present) | Hazard hrs (future) | Risk rank (both) |
|---|---|---:|---:|---:|
| Kampong Lama | hotspot | 42 | 249 | 1 |
| Dhobi Lines | hotspot | 26 | 217 | 2–3 |
| Fuzhou Lanes | hotspot | 22 | 212 | 2–3 |
| Mlima Moto | hotspot | 5 | 149 | 4 |
| Lusitano Square | core | 5 | 129 | 5 |
| Victoria Exchange | core | 5 | 120 | 6 |
| Jade Gardens | refuge | 62 | 260 | 7 (tied last) |
| Taman Melati | refuge | 47 | 243 | 7 (tied last) |
| Serendib Rise | refuge | 26 | 205 | 7 (tied last) |
| Zheng He Towers | core | 2 | 77 | 7 (tied last) |

**Headline finding:** the hottest neighbourhoods are not the highest-risk ones. The
low-rise *refuge* neighbourhoods post the most dangerous-heat hours in both scenarios
(weak turbulent mixing under NARP), but with zero exposed daytime population they rank
last on risk. The dense informal *hotspot* neighbourhoods have far fewer hazard hours
yet rank highest risk, driven by exposure and vulnerability. Critically, **the risk
ranking is essentially unchanged between present and the +2.5°C future**, even though
dangerous-heat hours rose 4–80x across neighbourhoods — exposure and vulnerability, not
hazard magnitude, are what separate top from bottom of this table.

Full write-up, method, and the caveats that travel with this result (illustrative
35°C dry-bulb threshold for a humid city, synthetic socio-economic layer, geometric-mean
combination choice, etc.) are on the published page:
https://jufufu.github.io/suews-hackathon-practice/

## Follow-on question (separate from the repo)

The user also asked about Local Climate Zones (LCZ) for the 10 neighbourhoods. The
dataset does not tag an LCZ directly, so one was derived from `neighbourhoods.yml`'s
`lambda_p` (building plan-area fraction = building footprint) and
`mean_building_height_m`, applying Stewart & Oke (2012) criteria. Notable finding: the
four `hotspot`-labelled neighbourhoods (described as "dense informal settlements") have
footprints of only 0.14–0.35 — well below the 0.6–0.9 that LCZ 7 (lightweight low-rise,
the standard informal-settlement signature) would imply. Their nearest LCZ is actually 9
(sparsely built) or the LCZ 6/8 boundary, not LCZ 7. This is a model-realism caveat worth
carrying into any real submission, separate from the heat-risk write-up. This
exploration was conversational and not persisted to the repo as a file.

## Outcome

- Repo: https://github.com/JuFufu/suews-hackathon-practice
- Pages: https://jufufu.github.io/suews-hackathon-practice/ — rebuilt and verified live
  (`status: built`, HTTP 200, new content confirmed present).
- Real SUEWS-driven heat-hazard and risk-bridge analysis completed end to end for both
  scenarios across all 10 UDA-city neighbourhoods.
