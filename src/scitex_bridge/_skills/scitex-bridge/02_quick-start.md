---
description: |
  [TOPIC] scitex-bridge Quick Start
  [DETAILS] Smallest example — annotate a matplotlib axes with a stats result via add_stat_to_axes.
tags: [scitex-bridge-quick-start]
---

# Quick Start

## Annotate a t-test result on a plot

```python
import matplotlib.pyplot as plt
import scitex_stats as stx_stats
import scitex_bridge

fig, ax = plt.subplots()
ax.boxplot([group_a, group_b], labels=["A", "B"])

result = stx_stats.test_ttest_ind(group_a, group_b, return_as="dict")
scitex_bridge.add_stat_to_axes(ax, result)   # adds p-value + significance bar
```

The bridge handles formatting (`p < 0.001`, `*`, `**`, `n.s.`) and
positioning (above the upper data point, in axes coords).

## Apply a batch of stat results

```python
results = [
    stx_stats.test_ttest_ind(a, b, return_as="dict"),
    stx_stats.test_ttest_ind(c, d, return_as="dict"),
]
scitex_bridge.add_stats_from_results(ax, results)
```

## Round-trip via vis FigureModel

```python
model = scitex_bridge.figure_to_vis_model(fig)
# requires scitex-vis installed
```

## Coordinate conventions

- **plt bridge** uses **axes coordinates** (0–1 normalized).
- **vis bridge** uses **data coordinates** (actual x/y values).

See `scitex_bridge.COORDINATE_SYSTEMS` for the full constant.
