"""Plot the diurnal Tair swing (present vs future forcing) used to explain
why dangerous-heat hours never occur at night (see docs/index.md)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "uda-city-hackathon" / "forcing"
COLS = ["iy", "id", "it", "imin", "qn", "qh", "qe", "qs", "qf", "U", "RH", "Tair",
        "pres", "rain", "kdown", "snow", "ldown", "fcld", "wuh", "xsmd", "lai",
        "kdiff", "kdir", "wdir"]
THRESHOLD = 35.0


def load(scenario):
    path = DATA / scenario / "UDA_2024_data_60.txt"
    df = pd.read_csv(path, sep=r"\s+", skiprows=1, names=COLS)
    df = df[df["Tair"] > -999]
    return df.groupby("it")["Tair"].agg(["min", "mean", "max"])


present = load("present_hot_humid")
future = load("future_hot_humid")

fig, ax = plt.subplots(figsize=(8, 4.5))
hours = present.index

ax.fill_between(hours, present["min"], present["max"], alpha=0.25, color="#1f77b4",
                 label="Present — range")
ax.plot(hours, present["mean"], color="#1f77b4", linewidth=2, label="Present — mean")

ax.fill_between(hours, future["min"], future["max"], alpha=0.25, color="#d62728",
                 label="+2.5°C future — range")
ax.plot(hours, future["mean"], color="#d62728", linewidth=2, label="+2.5°C future — mean")

ax.axhline(THRESHOLD, color="black", linestyle="--", linewidth=1,
            label=f"Dangerous-heat threshold ({THRESHOLD:.0f}°C)")
ax.axvspan(6, 18, color="khaki", alpha=0.15, label="Daytime (06:00–18:00)")

ax.set_xlabel("Hour of day (local time)")
ax.set_ylabel("2 m air temperature, Tair (°C)")
ax.set_title("UDA-city diurnal temperature swing: present vs. +2.5°C future")
ax.set_xticks(range(0, 24, 3))
ax.set_xlim(0, 23)
ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.32), ncol=2, fontsize=8, frameon=False)
fig.tight_layout()

out = Path(__file__).resolve().parent.parent / "docs" / "img" / "diurnal_swing.png"
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=150)
print(f"wrote {out}")
