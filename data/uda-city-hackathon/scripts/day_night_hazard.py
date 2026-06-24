"""Ad-hoc check: is dangerous heat concentrated by day or by night?

Splits dangerous-heat hours (hourly-mean T2 > threshold) into local
day (06:00-18:00) and night (18:00-06:00) buckets per neighbourhood,
for the present scenario, after the standard 14-day spin-up discard.
"""
import warnings
warnings.filterwarnings("ignore")
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from risk_bridge import run_scenario_live, REPO_ROOT

THRESHOLD = 35.0
SPINUP_DAYS = 14

results = run_scenario_live(REPO_ROOT / "uda-city.yml", None)

print(f"{'grid':>4} {'day_hrs':>8} {'night_hrs':>10} {'total':>7}")
for grid in results.index.get_level_values(0).unique():
    t2 = results.loc[grid][("SUEWS", "T2")].dropna()
    t2 = t2.iloc[SPINUP_DAYS * 288:]
    hourly = t2.resample("h").mean()
    is_hot = hourly > THRESHOLD
    hour_of_day = hourly.index.hour
    day_mask = (hour_of_day >= 6) & (hour_of_day < 18)
    day_hrs = int((is_hot & day_mask).sum())
    night_hrs = int((is_hot & ~day_mask).sum())
    print(f"{grid:>4} {day_hrs:>8} {night_hrs:>10} {day_hrs+night_hrs:>7}")
