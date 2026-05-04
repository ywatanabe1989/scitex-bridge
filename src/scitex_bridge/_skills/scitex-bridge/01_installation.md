---
description: |
  [TOPIC] scitex-bridge Installation
  [DETAILS] pip install scitex-bridge; depends on scitex-stats + matplotlib; smoke verify protocol version.
tags: [scitex-bridge-installation]
---

# Installation

## Standard

```bash
pip install scitex-bridge
```

Pulls `matplotlib` and `scitex-stats` (for the stats→plt adapters).
`scitex-vis` and `figrecipe` are optional companions — when installed,
the corresponding bridge functions become functional; otherwise they
raise a clear `ImportError` at call time.

## Umbrella

```bash
pip install scitex            # also exposes the same module as scitex.bridge
```

`pip install scitex-bridge` alone does NOT make `import scitex.bridge`
work — install the umbrella for that form. See
`../../general/02_interface-python-api.md`.

## Verify

```bash
python -c "import scitex_bridge; print(scitex_bridge.__version__, scitex_bridge.BRIDGE_PROTOCOL_VERSION)"
```

Expected: a version string and the bridge protocol version (e.g.
`1.0.0`).

## Optional companions

| Companion       | Unlocks                                                  |
|-----------------|----------------------------------------------------------|
| `figrecipe`     | `save_with_recipe`, `load_recipe`                        |
| `scitex-vis`    | `figure_to_vis_model`, `axes_to_vis_axes`, vis adapters  |

Check at runtime:

```python
import scitex_bridge
scitex_bridge.has_figrecipe()       # bool
scitex_bridge.FIGRECIPE_AVAILABLE   # const
```
