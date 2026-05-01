#!/usr/bin/env python3
"""Tests for scitex_bridge._figrecipe public surface.

The module is a thin adapter over an *optional* figrecipe dependency and an
*optional* scitex.io.bundle storage backend. Tests exercise:
  - has_figrecipe() returns a bool
  - save_with_recipe() degrades gracefully when storage isn't available
  - load_recipe() raises ImportError when figrecipe is absent
  - _save_figure_image() writes a real PNG given a vanilla matplotlib fig
  - _capture_figure_state() syncs figsize/dpi onto the record
"""

from pathlib import Path
from types import SimpleNamespace

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pytest

import scitex_bridge._figrecipe as fr_mod
from scitex_bridge._figrecipe import (
    _capture_figure_state,
    _save_figure_image,
    has_figrecipe,
    load_recipe,
    save_with_recipe,
)


@pytest.fixture
def mpl_fig():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])
    yield fig
    plt.close(fig)


class TestHasFigrecipe:
    def test_returns_bool(self):
        assert isinstance(has_figrecipe(), bool)

    def test_tracks_module_flag(self):
        # has_figrecipe is a thin wrapper around the module-level constant
        assert has_figrecipe() is fr_mod.FIGRECIPE_AVAILABLE


class TestSaveWithRecipe:
    def test_returns_empty_when_storage_unavailable(
        self, mpl_fig, tmp_path, monkeypatch
    ):
        # The bundle storage path is gated on scitex.io.bundle being importable.
        # Force the ImportError branch to verify graceful degradation.
        import builtins

        real_import = builtins.__import__

        def fake_import(name, *a, **kw):
            if name.startswith("scitex.io.bundle"):
                raise ImportError("forced for test")
            return real_import(name, *a, **kw)

        monkeypatch.setattr(builtins, "__import__", fake_import)
        result = save_with_recipe(mpl_fig, tmp_path / "bundle")
        assert result == {}

    def test_returns_dict(self, mpl_fig, tmp_path):
        # Whether or not storage is available, the public return is a dict.
        result = save_with_recipe(mpl_fig, tmp_path / "bundle")
        assert isinstance(result, dict)


class TestLoadRecipe:
    def test_raises_import_error_when_figrecipe_unavailable(
        self, tmp_path, monkeypatch
    ):
        monkeypatch.setattr(fr_mod, "FIGRECIPE_AVAILABLE", False)
        with pytest.raises(ImportError, match="figrecipe is required"):
            load_recipe(tmp_path / "recipe.yaml")


class TestSaveFigureImage:
    def test_writes_png_for_vanilla_mpl_fig(self, mpl_fig, tmp_path):
        out = tmp_path / "plot.png"
        _save_figure_image(mpl_fig, out, dpi=72)
        assert out.exists()
        assert out.stat().st_size > 0

    def test_uses_savefig_attr_when_present(self, tmp_path):
        # Object that exposes its own savefig() — the helper should call it.
        calls = []

        class Custom:
            def savefig(self, p, **kw):
                calls.append((Path(p), kw))
                Path(p).write_bytes(b"\x89PNG\r\n\x1a\n")

        out = tmp_path / "out.png"
        _save_figure_image(Custom(), out, dpi=99, facecolor="white")
        assert len(calls) == 1
        assert calls[0][0] == out
        assert calls[0][1]["dpi"] == 99
        assert calls[0][1]["facecolor"] == "white"


class TestCaptureFigureState:
    def test_updates_figsize_and_dpi(self, mpl_fig):
        record = SimpleNamespace(figsize=None, dpi=None)
        _capture_figure_state(mpl_fig, record)
        assert isinstance(record.figsize, list)
        assert len(record.figsize) == 2
        assert record.dpi == int(mpl_fig.dpi)

    def test_swallows_errors_silently(self):
        # Passing a non-figure object must not raise (helper is best-effort).
        _capture_figure_state(object(), SimpleNamespace())


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
