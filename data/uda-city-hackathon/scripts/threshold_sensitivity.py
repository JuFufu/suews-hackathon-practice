"""How sensitive is dangerous-heat-hours to exactly where the threshold sits,
given the shape of the diurnal T2 curve? Uses the actual SUEWS output (not
raw forcing) for the present scenario's worst-hazard grid (Jade Gardens,
gridiv=1)."""
import warnings
warnings.filterwarnings("ignore")
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from risk_bridge import run_scenario_live, REPO_ROOT

SPINUP_DAYS = 14
GRID = 1

results = run_scenario_live(REPO_ROOT / "uda-city.yml", None)
t2 = results.loc[GRID][("SUEWS", "T2")].dropna()
t2 = t2.iloc[SPINUP_DAYS * 288:]
hourly = t2.resample("h").mean()

print("Diurnal mean T2 by hour (Jade Gardens, present):")
for h in range(0, 24, 2):
    sub = hourly[hourly.index.hour == h]
    print(f"  {h:02d}:00  mean={sub.mean():.2f}C  max={sub.max():.2f}C")

print("\nDangerous-heat hours at nearby thresholds (same data, threshold only changes):")
for thr in [33.0, 34.0, 35.0, 36.0, 37.0]:
    hrs = int((hourly > thr).sum())
    print(f"  threshold {thr:.0f}C -> {hrs} hours")
