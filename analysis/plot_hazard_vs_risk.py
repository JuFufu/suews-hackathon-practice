"""Plot hazard vs. risk per neighbourhood — the core 'hottest != highest-risk'
finding, designed to read clearly with minimal text (for a non-specialist /
cross-language audience). See docs/index.md."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
df = pd.read_csv(ROOT / "analysis" / "outputs" / "risk_present.csv")

COLORS = {"refuge": "#2ca02c", "core": "#1f77b4", "hotspot": "#d62728"}

fig, ax = plt.subplots(figsize=(8, 6))

for _, row in df.iterrows():
    ax.scatter(
        row["dangerous_heat_hours"], row["risk_index"],
        s=row["population_day"] * 3.5,
        color=COLORS[row["type"]], alpha=0.85, edgecolor="white", linewidth=1.2,
        zorder=3,
    )
    ax.annotate(
        row["name"], (row["dangerous_heat_hours"], row["risk_index"]),
        xytext=(8, 6), textcoords="offset points", fontsize=9,
    )

ax.set_xlabel("Heat hazard  →  dangerous-heat hours (present scenario)", fontsize=11)
ax.set_ylabel("Heat risk  →  risk index (0 = lowest, 1 = highest)", fontsize=11)
ax.set_title("Hottest ≠ highest-risk: heat hazard vs. socio-economic heat risk",
              fontsize=13, fontweight="bold")

ax.annotate("HOTTEST,\nLOWEST RISK\n(few people exposed)",
            xy=(0.97, 0.22), xycoords="axes fraction", ha="right", va="bottom",
            fontsize=10, color="#2ca02c", fontweight="bold")
ax.annotate("LESS HOT,\nHIGHEST RISK\n(many people, low capacity to cope)",
            xy=(0.04, 0.97), xycoords="axes fraction", ha="left", va="top",
            fontsize=10, color="#d62728", fontweight="bold")

handles = [plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=c,
                       markersize=10, label=t.capitalize())
           for t, c in COLORS.items()]
handles.append(plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="grey",
                           markersize=6, label="Bubble size = daytime population"))
ax.legend(handles=handles, loc="center right", fontsize=9, frameon=False)

ax.grid(alpha=0.2)
ax.set_xlim(-5, 70)
ax.set_ylim(-0.05, 1.1)
fig.tight_layout()

out = ROOT / "docs" / "img" / "hazard_vs_risk.png"
fig.savefig(out, dpi=150)
print(f"wrote {out}")
