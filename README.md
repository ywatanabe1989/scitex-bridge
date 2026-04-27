# scitex-bridge

<!-- scitex-badges:start -->
[![PyPI](https://img.shields.io/pypi/v/scitex-bridge.svg)](https://pypi.org/project/scitex-bridge/)
[![Python](https://img.shields.io/pypi/pyversions/scitex-bridge.svg)](https://pypi.org/project/scitex-bridge/)
[![Tests](https://github.com/ywatanabe1989/scitex-bridge/actions/workflows/test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-bridge/actions/workflows/test.yml)
[![Install Test](https://github.com/ywatanabe1989/scitex-bridge/actions/workflows/install-test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-bridge/actions/workflows/install-test.yml)
[![Coverage](https://codecov.io/gh/ywatanabe1989/scitex-bridge/graph/badge.svg)](https://codecov.io/gh/ywatanabe1989/scitex-bridge)
[![Docs](https://readthedocs.org/projects/scitex-bridge/badge/?version=latest)](https://scitex-bridge.readthedocs.io/en/latest/)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
<!-- scitex-badges:end -->


Cross-module adapters between scitex.stats / matplotlib / vis-FigureModel, extracted from the [SciTeX](https://github.com/ywatanabe1989/scitex-python) ecosystem as a standalone package.

## Install

```bash
pip install scitex-bridge
```

## API

```python
import scitex_bridge as br

# Add stats results to either backend (auto-detects)
br.add_stats_from_results(target, stat_results, format_style="asterisk")

# Stats → matplotlib annotation
br.add_stat_to_axes(ax, stat_result)
br.format_stat_for_plot(stat_result, style="asterisk")
br.extract_stats_from_axes(ax)

# Stats → vis (FigureModel)
br.stat_result_to_annotation(stat_result)
br.add_stats_to_figure_model(fig_model, stat_results)
br.position_stat_annotation(fig_model, stat_result, prefer_corner="top-right")

# plt ↔ vis
br.matplotlib_to_figure_model(fig)
br.figure_model_to_matplotlib(fig_model)

# Protocols (Position duck-typing target)
from scitex_bridge import Position
```

## Status

Standalone fork of `scitex.bridge`. Deps: matplotlib + scipy.

Decoupling notes:
- `scitex.io.bundle.kinds._stats.Position` → vendored as a tiny dataclass in
  `_compat.py`. When `scitex` (umbrella) is installed, the real Position is
  preferred so produced objects round-trip cleanly through bundle code paths.
- The optional `scitex.io.bundle.kinds._plot._models` imports remain inside
  `try/except ImportError` so the package works fully standalone.

The umbrella package's `scitex.bridge` import path is preserved via a
`sys.modules`-alias bridge.

## License

AGPL-3.0-only (see [LICENSE](./LICENSE)).
