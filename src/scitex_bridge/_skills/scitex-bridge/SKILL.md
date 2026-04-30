---
name: scitex-bridge
description: Cross-module adapters (stats↔plt, stats↔vis, plt↔vis). Converts `scitex_stats` test results into matplotlib annotations (p-values, significance bars, effect-size labels) without re-implementing the formatter in every plotting helper. Drop-in replacement for `ax.text(x, y, f'p={p:.3f}*')` boilerplate.
primary_interface: python
interfaces:
  python: 2
  cli: 0
  mcp: 0
  skills: 2
  hook: 0
  http: 0
canonical-location: scitex-bridge/src/scitex_bridge/_skills/scitex-bridge/SKILL.md
tags: [scitex-bridge, scitex-package]
---

> **Interfaces:** Python ⭐⭐ · CLI — · MCP — · Skills ⭐⭐ · Hook — · HTTP —

# scitex-bridge

Cross-module adapters (stats↔plt, stats↔vis, plt↔vis). Converts `scitex_stats` test results into matplotlib annotations (p-values, significance bars, effect-size labels) without re-implementing the formatter in every plotting helper. Drop-in replacement for `ax.text(x, y, f'p={p:.3f}*')` boilerplate.

See README.md and the package's public `__init__.py` for the full
function list. This skill leaf exists so agents discover the package
exists and roughly what shape it has — refer to the source for
signatures.
