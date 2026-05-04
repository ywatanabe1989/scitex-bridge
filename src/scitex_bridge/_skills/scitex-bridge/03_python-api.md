---
description: |
  [TOPIC] scitex-bridge Python API
  [DETAILS] Top-level public callables — protocol, stats↔plt, stats↔vis, plt↔vis, figrecipe integration.
tags: [scitex-bridge-python-api]
---

# Python API

Public surface re-exported from `scitex_bridge` (see `__all__`).

## Protocol

| Name                              | Purpose                                          |
|-----------------------------------|--------------------------------------------------|
| `__version__`                     | Installed package version                        |
| `BRIDGE_PROTOCOL_VERSION`         | Bridge protocol version (e.g. `1.0.0`)           |
| `ProtocolInfo`                    | Dataclass — bridge metadata payload              |
| `check_protocol_compatibility(v)` | Check producer / consumer protocol compatibility |
| `add_protocol_metadata(obj)`      | Attach bridge protocol info to an object         |
| `extract_protocol_metadata(obj)`  | Read bridge protocol info from an object         |
| `COORDINATE_SYSTEMS`              | Constant — plt vs vis coord conventions          |

## Stats ↔ Plt

| Name                          | Purpose                                              |
|-------------------------------|------------------------------------------------------|
| `add_stat_to_axes(ax, res)`   | Add p-value / significance bar to a matplotlib axes  |
| `extract_stats_from_axes(ax)` | Pull bridge-emitted stats annotations back out       |
| `format_stat_for_plot(res)`   | Format `p`, stars, effect size for plot text         |

## Stats ↔ Vis

| Name                              | Purpose                                       |
|-----------------------------------|-----------------------------------------------|
| `stat_result_to_annotation(res)`  | Convert stats dict to vis Annotation          |
| `add_stats_to_figure_model(fm)`   | Attach annotations to a vis FigureModel       |
| `position_stat_annotation(...)`   | Compute placement in data coords              |

## Plt ↔ Vis

| Name                              | Purpose                                       |
|-----------------------------------|-----------------------------------------------|
| `figure_to_vis_model(fig)`        | matplotlib `Figure` → vis `FigureModel`       |
| `axes_to_vis_axes(ax)`            | matplotlib `Axes` → vis `AxesModel`           |
| `tracking_to_plot_configs(track)` | scitex-plt tracking dict → vis plot configs   |
| `collect_figure_data(fig)`        | Pull all data series out of a figure          |

## Helpers / FigRecipe

| Name                          | Purpose                                              |
|-------------------------------|------------------------------------------------------|
| `add_stats_from_results(ax, results)` | Batch annotate from a list of stats results  |
| `save_with_recipe(...)`       | Save figure + figrecipe YAML (requires figrecipe)    |
| `load_recipe(path)`           | Load a figrecipe YAML                                |
| `has_figrecipe()`             | Bool — figrecipe importable                          |
| `FIGRECIPE_AVAILABLE`         | Const equivalent of `has_figrecipe()`                |

## Design notes

- All functions use only **public APIs** of each module — no reaching
  into private state.
- All transformations validate against the bridge schema.
- See module docstring for the Protocol Version evolution rules.
