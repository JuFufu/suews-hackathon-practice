# SUEWS Hackathon — Practice Repo

This is a **practice repository** ahead of the SUEWS Community Hackathon (24 June 2026,
UCL East). It is not a hackathon submission: the focus-city dataset and heat-to-risk
bridge are released at kickoff on the day.

## Pipeline smoke test

To confirm the tooling works end to end before the event, a small SUEWS simulation was
run via [supy](https://supy.readthedocs.io/) (the Python interface used by suews-agent)
using its bundled sample dataset:

- SUEWS version: `2026.6.5`
- Simulation period: 2012-01-01 00:05 to 2012-01-02 00:00 (1 day, 5-min timestep)
- Output: surface energy balance terms (QN, QH, QE, surface temperature) produced
  successfully — see [`analysis/smoke_test.py`](../analysis/smoke_test.py) and
  [`analysis/smoke_test_output.txt`](../analysis/smoke_test_output.txt).

On the day, this page will instead tell the story of the real challenge:

- The question asked.
- How SUEWS was configured via the suews-agent for the focus city.
- The heat-hazard result and the socio-economic risk indicator.
- Where the hazard-to-indicator bridge holds, and where it breaks.

## Citing SUEWS

- Järvi, L., Grimmond, C.S.B. & Christen, A. (2011). The Surface Urban Energy and Water
  Balance Scheme (SUEWS): Evaluation in Los Angeles and Vancouver. *Journal of
  Hydrology*, 411(3–4), 219–237. https://doi.org/10.1016/j.jhydrol.2011.10.001
- Ward, H.C., Kotthaus, S., Järvi, L. & Grimmond, C.S.B. (2016). Surface Urban Energy and
  Water Balance Scheme (SUEWS): Development and evaluation at two UK sites. *Urban
  Climate*, 18, 1–32. https://doi.org/10.1016/j.uclim.2016.05.001
