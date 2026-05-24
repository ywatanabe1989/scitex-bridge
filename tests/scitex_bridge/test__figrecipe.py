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
    def test_returns_bool_isinstance_has_figrecipe_bool(self):
        # Arrange
        # Act
        # Assert
        assert isinstance(has_figrecipe(), bool)

    def test_tracks_module_flag(self):
        # has_figrecipe is a thin wrapper around the module-level constant
        # Arrange
        # Act
        # Assert
        assert has_figrecipe() is fr_mod.FIGRECIPE_AVAILABLE


class TestSaveWithRecipe:
    def test_returns_empty_when_storage_resolver_yields_none(self, mpl_fig, tmp_path):
        # The bundle storage path is gated on scitex.io.bundle being importable.
        # Inject a resolver that reports the dependency as absent (returns None)
        # to verify graceful degradation regardless of what is installed.
        # Arrange
        def storage_absent():
            return None

        # Act
        result = save_with_recipe(
            mpl_fig, tmp_path / "bundle", storage_resolver=storage_absent
        )
        # Assert
        assert result == {}

    def test_returns_dict_result_is_dict(self, mpl_fig, tmp_path):
        # Whether or not storage is available, the public return is a dict.
        # Arrange
        # Act
        result = save_with_recipe(mpl_fig, tmp_path / "bundle")
        # Assert
        assert isinstance(result, dict)


class TestLoadRecipe:
    def test_raises_import_error_when_figrecipe_unavailable(self, tmp_path):
        # Inject the availability flag as False (rather than rewriting the
        # module global) to exercise the missing-dependency branch.
        # Arrange
        recipe_path = tmp_path / "recipe.yaml"
        # Act
        ctx = pytest.raises(ImportError, match="figrecipe is required")
        # Assert
        with ctx:
            load_recipe(recipe_path, figrecipe_available=False)


class TestSaveFigureImage:
    def test_writes_png_for_vanilla_mpl_fig_out_exists(self, mpl_fig, tmp_path):
        # Arrange
        # Arrange
        out = tmp_path / "plot.png"
        # Act
        _save_figure_image(mpl_fig, out, dpi=72)
        # Act
        # Assert
        # Assert
        assert out.exists()

    def test_writes_png_for_vanilla_mpl_fig_out_stat_st_size_0(self, mpl_fig, tmp_path):
        # Arrange
        # Arrange
        out = tmp_path / "plot.png"
        # Act
        _save_figure_image(mpl_fig, out, dpi=72)
        # Act
        # Assert
        # Assert
        assert out.stat().st_size > 0

    def test_uses_savefig_attr_when_present_len_calls_is_1(self, tmp_path):
        # Object that exposes its own savefig() — the helper should call it.
        # Arrange
        # Arrange
        calls = []

        class Custom:
            def savefig(self, p, **kw):
                calls.append((Path(p), kw))
                Path(p).write_bytes(b"\x89PNG\r\n\x1a\n")

        out = tmp_path / "out.png"
        # Act
        _save_figure_image(Custom(), out, dpi=99, facecolor="white")
        # Act
        # Assert
        # Assert
        assert len(calls) == 1

    def test_uses_savefig_attr_when_present_calls_0_0_out(self, tmp_path):
        # Object that exposes its own savefig() — the helper should call it.
        # Arrange
        # Arrange
        calls = []

        class Custom:
            def savefig(self, p, **kw):
                calls.append((Path(p), kw))
                Path(p).write_bytes(b"\x89PNG\r\n\x1a\n")

        out = tmp_path / "out.png"
        # Act
        _save_figure_image(Custom(), out, dpi=99, facecolor="white")
        # Act
        # Assert
        # Assert
        assert calls[0][0] == out

    def test_uses_savefig_attr_when_present_calls_0_1_dpi_99(self, tmp_path):
        # Object that exposes its own savefig() — the helper should call it.
        # Arrange
        # Arrange
        calls = []

        class Custom:
            def savefig(self, p, **kw):
                calls.append((Path(p), kw))
                Path(p).write_bytes(b"\x89PNG\r\n\x1a\n")

        out = tmp_path / "out.png"
        # Act
        _save_figure_image(Custom(), out, dpi=99, facecolor="white")
        # Act
        # Assert
        # Assert
        assert calls[0][1]["dpi"] == 99

    def test_uses_savefig_attr_when_present_calls_0_1_facecolor_white(self, tmp_path):
        # Object that exposes its own savefig() — the helper should call it.
        # Arrange
        # Arrange
        calls = []

        class Custom:
            def savefig(self, p, **kw):
                calls.append((Path(p), kw))
                Path(p).write_bytes(b"\x89PNG\r\n\x1a\n")

        out = tmp_path / "out.png"
        # Act
        _save_figure_image(Custom(), out, dpi=99, facecolor="white")
        # Act
        # Assert
        # Assert
        assert calls[0][1]["facecolor"] == "white"


class TestCaptureFigureState:
    def test_updates_figsize_and_dpi_record_figsize_is_list(self, mpl_fig):
        # Arrange
        # Arrange
        record = SimpleNamespace(figsize=None, dpi=None)
        # Act
        _capture_figure_state(mpl_fig, record)
        # Act
        # Assert
        # Assert
        assert isinstance(record.figsize, list)

    def test_updates_figsize_and_dpi_len_record_figsize_is_2(self, mpl_fig):
        # Arrange
        # Arrange
        record = SimpleNamespace(figsize=None, dpi=None)
        # Act
        _capture_figure_state(mpl_fig, record)
        # Act
        # Assert
        # Assert
        assert len(record.figsize) == 2

    def test_updates_figsize_and_dpi_record_dpi_equals_int_mpl_fig_dpi(self, mpl_fig):
        # Arrange
        # Arrange
        record = SimpleNamespace(figsize=None, dpi=None)
        # Act
        _capture_figure_state(mpl_fig, record)
        # Act
        # Assert
        # Assert
        assert record.dpi == int(mpl_fig.dpi)

    def test_swallows_errors_silently_for_non_figure_input(self):
        # Passing a non-figure object must not raise (helper is best-effort).
        # The record must be left untouched (figsize stays None).
        # Arrange
        record = SimpleNamespace(figsize=None, dpi=None)
        # Act
        _capture_figure_state(object(), record)
        # Assert
        assert record.figsize is None


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
