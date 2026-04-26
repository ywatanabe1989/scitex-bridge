"""Tiny vendored copies of scitex.io.bundle dataclasses we need.

Keeps scitex-bridge free of scitex.* runtime deps for the core code paths.
When scitex (umbrella) is installed, callers can still pass the real
``scitex.io.bundle.kinds._stats.Position`` — duck-typing handles it.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Literal, Optional

UnitType = Literal["mm", "px", "inch", "data"]


@dataclass
class Position:
    """Position specification with unit support for GUI integration.

    Vendored from ``scitex.io.bundle.kinds._stats.Position``. Supports multiple
    coordinate systems (matplotlib mm, Fabric.js px, data coordinates).
    """

    x: float
    y: float
    unit: UnitType = "mm"
    relative_to: Optional[str] = None
    offset: Optional[Dict[str, float]] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "x": self.x,
            "y": self.y,
            "unit": self.unit,
            "relative_to": self.relative_to,
            "offset": self.offset,
        }
