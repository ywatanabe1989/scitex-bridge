#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: ./tests/scitex/bridge/test__protocol.py
"""Tests for bridge protocol versioning."""

import pytest

from scitex_bridge._protocol import (
    BRIDGE_PROTOCOL_VERSION,
    COORDINATE_SYSTEMS,
    ProtocolInfo,
    add_protocol_metadata,
    check_protocol_compatibility,
    extract_protocol_metadata,
    parse_version,
)


class TestProtocolVersion:
    """Tests for protocol version constant."""

    def test_version_format_len_parts_is_3(self):
        # Arrange
        # Arrange
        # Act
        parts = BRIDGE_PROTOCOL_VERSION.split(".")
        # Act
        # Assert
        # Assert
        assert len(parts) == 3

    def test_version_format_all_part_isdigit_for_part_in_parts(self):
        # Arrange
        # Arrange
        # Act
        parts = BRIDGE_PROTOCOL_VERSION.split(".")
        # Act
        # Assert
        # Assert
        assert all(part.isdigit() for part in parts)


    def test_current_version_bridge_protocol_version_equals_n_1_0_0(self):
        """Current version should be 1.0.0."""
        # Arrange
        # Act
        # Assert
        assert BRIDGE_PROTOCOL_VERSION == "1.0.0"


class TestParseVersion:
    """Tests for version parsing."""

    def test_full_version_major_equals_n_1(self):
        # Arrange
        # Arrange
        # Act
        major, minor, patch = parse_version("1.2.3")
        # Act
        # Assert
        # Assert
        assert major == 1

    def test_full_version_minor_equals_n_2(self):
        # Arrange
        # Arrange
        # Act
        major, minor, patch = parse_version("1.2.3")
        # Act
        # Assert
        # Assert
        assert minor == 2

    def test_full_version_patch_equals_n_3(self):
        # Arrange
        # Arrange
        # Act
        major, minor, patch = parse_version("1.2.3")
        # Act
        # Assert
        # Assert
        assert patch == 3


    def test_partial_version_major_equals_n_2(self):
        # Arrange
        # Arrange
        # Act
        major, minor, patch = parse_version("2.1")
        # Act
        # Assert
        # Assert
        assert major == 2

    def test_partial_version_minor_equals_n_1(self):
        # Arrange
        # Arrange
        # Act
        major, minor, patch = parse_version("2.1")
        # Act
        # Assert
        # Assert
        assert minor == 1

    def test_partial_version_patch_equals_n_0(self):
        # Arrange
        # Arrange
        # Act
        major, minor, patch = parse_version("2.1")
        # Act
        # Assert
        # Assert
        assert patch == 0


    def test_major_only_major_equals_n_3(self):
        # Arrange
        # Arrange
        # Act
        major, minor, patch = parse_version("3")
        # Act
        # Assert
        # Assert
        assert major == 3

    def test_major_only_minor_equals_n_0(self):
        # Arrange
        # Arrange
        # Act
        major, minor, patch = parse_version("3")
        # Act
        # Assert
        # Assert
        assert minor == 0

    def test_major_only_patch_equals_n_0(self):
        # Arrange
        # Arrange
        # Act
        major, minor, patch = parse_version("3")
        # Act
        # Assert
        # Assert
        assert patch == 0



class TestProtocolCompatibility:
    """Tests for protocol compatibility checking."""

    def test_same_version_compatible_is_compat_is_true(self):
        # Arrange
        # Arrange
        # Act
        is_compat, msg = check_protocol_compatibility("1.0.0", "1.0.0")
        # Act
        # Assert
        # Assert
        assert is_compat is True

    def test_same_version_compatible_msg_is_none(self):
        # Arrange
        # Arrange
        # Act
        is_compat, msg = check_protocol_compatibility("1.0.0", "1.0.0")
        # Act
        # Assert
        # Assert
        assert msg is None


    def test_older_minor_compatible_is_compat_is_true(self):
        # Arrange
        # Arrange
        # Act
        is_compat, msg = check_protocol_compatibility("1.0.0", "1.1.0")
        # Act
        # Assert
        # Assert
        assert is_compat is True

    def test_older_minor_compatible_msg_is_none(self):
        # Arrange
        # Arrange
        # Act
        is_compat, msg = check_protocol_compatibility("1.0.0", "1.1.0")
        # Act
        # Assert
        # Assert
        assert msg is None


    def test_newer_minor_warning_is_compat_is_true(self):
        # Arrange
        # Arrange
        # Act
        is_compat, msg = check_protocol_compatibility("1.2.0", "1.0.0")
        # Act
        # Assert
        # Assert
        assert is_compat is True

    def test_newer_minor_warning_msg_is_not_none(self):
        # Arrange
        # Arrange
        # Act
        is_compat, msg = check_protocol_compatibility("1.2.0", "1.0.0")
        # Act
        # Assert
        # Assert
        assert msg is not None

    def test_newer_minor_warning_newer_in_msg_lower(self):
        # Arrange
        # Arrange
        # Act
        is_compat, msg = check_protocol_compatibility("1.2.0", "1.0.0")
        # Act
        # Assert
        # Assert
        assert "newer" in msg.lower()


    def test_major_mismatch_incompatible_is_compat_is_false(self):
        # Arrange
        # Arrange
        # Act
        is_compat, msg = check_protocol_compatibility("2.0.0", "1.0.0")
        # Act
        # Assert
        # Assert
        assert is_compat is False

    def test_major_mismatch_incompatible_msg_is_not_none(self):
        # Arrange
        # Arrange
        # Act
        is_compat, msg = check_protocol_compatibility("2.0.0", "1.0.0")
        # Act
        # Assert
        # Assert
        assert msg is not None

    def test_major_mismatch_incompatible_major_in_msg_lower(self):
        # Arrange
        # Arrange
        # Act
        is_compat, msg = check_protocol_compatibility("2.0.0", "1.0.0")
        # Act
        # Assert
        # Assert
        assert "major" in msg.lower()


    def test_current_version_default(self):
        """Should use BRIDGE_PROTOCOL_VERSION as default."""
        # Arrange
        # Act
        is_compat, msg = check_protocol_compatibility(BRIDGE_PROTOCOL_VERSION)
        # Assert
        assert is_compat is True


class TestProtocolInfo:
    """Tests for ProtocolInfo dataclass."""

    def test_default_values_info_version_equals_bridge_protocol_version(self):
        # Arrange
        # Arrange
        # Act
        info = ProtocolInfo()
        # Act
        # Assert
        # Assert
        assert info.version == BRIDGE_PROTOCOL_VERSION

    def test_default_values_info_coordinate_system_equals_data(self):
        # Arrange
        # Arrange
        # Act
        info = ProtocolInfo()
        # Act
        # Assert
        # Assert
        assert info.coordinate_system == "data"


    def test_custom_values_info_source_module_equals_stats(self):
        # Arrange
        # Arrange
        # Act
        info = ProtocolInfo(
            source_module="stats",
            target_module="vis",
            coordinate_system="axes",
        )
        # Act
        # Assert
        # Assert
        assert info.source_module == "stats"

    def test_custom_values_info_target_module_equals_vis(self):
        # Arrange
        # Arrange
        # Act
        info = ProtocolInfo(
            source_module="stats",
            target_module="vis",
            coordinate_system="axes",
        )
        # Act
        # Assert
        # Assert
        assert info.target_module == "vis"

    def test_custom_values_info_coordinate_system_equals_axes(self):
        # Arrange
        # Arrange
        # Act
        info = ProtocolInfo(
            source_module="stats",
            target_module="vis",
            coordinate_system="axes",
        )
        # Act
        # Assert
        # Assert
        assert info.coordinate_system == "axes"


    def test_to_dict_d_bridge_protocol_version_bridge_protocol_version(self):
        # Arrange
        # Arrange
        info = ProtocolInfo(source_module="plt", target_module="vis")
        # Act
        d = info.to_dict()
        # Act
        # Assert
        # Assert
        assert d["bridge_protocol_version"] == BRIDGE_PROTOCOL_VERSION

    def test_to_dict_d_source_module_plt(self):
        # Arrange
        # Arrange
        info = ProtocolInfo(source_module="plt", target_module="vis")
        # Act
        d = info.to_dict()
        # Act
        # Assert
        # Assert
        assert d["source_module"] == "plt"

    def test_to_dict_d_target_module_vis(self):
        # Arrange
        # Arrange
        info = ProtocolInfo(source_module="plt", target_module="vis")
        # Act
        d = info.to_dict()
        # Act
        # Assert
        # Assert
        assert d["target_module"] == "vis"


    def test_from_dict_info_version_equals_n_1_0_0(self):
        # Arrange
        # Arrange
        d = {
            "bridge_protocol_version": "1.0.0",
            "source_module": "stats",
            "target_module": "plt",
            "coordinate_system": "mm",
        }
        # Act
        info = ProtocolInfo.from_dict(d)
        # Act
        # Assert
        # Assert
        assert info.version == "1.0.0"

    def test_from_dict_info_source_module_equals_stats(self):
        # Arrange
        # Arrange
        d = {
            "bridge_protocol_version": "1.0.0",
            "source_module": "stats",
            "target_module": "plt",
            "coordinate_system": "mm",
        }
        # Act
        info = ProtocolInfo.from_dict(d)
        # Act
        # Assert
        # Assert
        assert info.source_module == "stats"

    def test_from_dict_info_target_module_equals_plt(self):
        # Arrange
        # Arrange
        d = {
            "bridge_protocol_version": "1.0.0",
            "source_module": "stats",
            "target_module": "plt",
            "coordinate_system": "mm",
        }
        # Act
        info = ProtocolInfo.from_dict(d)
        # Act
        # Assert
        # Assert
        assert info.target_module == "plt"

    def test_from_dict_info_coordinate_system_equals_mm(self):
        # Arrange
        # Arrange
        d = {
            "bridge_protocol_version": "1.0.0",
            "source_module": "stats",
            "target_module": "plt",
            "coordinate_system": "mm",
        }
        # Act
        info = ProtocolInfo.from_dict(d)
        # Act
        # Assert
        # Assert
        assert info.coordinate_system == "mm"



class TestProtocolMetadata:
    """Tests for protocol metadata utilities."""

    def test_add_metadata_bridge_protocol_in_result(self):
        # Arrange
        # Arrange
        data = {"x": 10, "y": 20}
        # Act
        result = add_protocol_metadata(data, "stats", "vis", "data")
        # Act
        # Assert
        # Assert
        assert "_bridge_protocol" in result

    def test_add_metadata_result_bridge_protocol_bridge_protocol_version_bridge_protoc(self):
        # Arrange
        # Arrange
        data = {"x": 10, "y": 20}
        # Act
        result = add_protocol_metadata(data, "stats", "vis", "data")
        # Act
        # Assert
        # Assert
        assert (
            result["_bridge_protocol"]["bridge_protocol_version"]
            == BRIDGE_PROTOCOL_VERSION
        )

    def test_add_metadata_result_bridge_protocol_source_module_stats(self):
        # Arrange
        # Arrange
        data = {"x": 10, "y": 20}
        # Act
        result = add_protocol_metadata(data, "stats", "vis", "data")
        # Act
        # Assert
        # Assert
        assert result["_bridge_protocol"]["source_module"] == "stats"

    def test_add_metadata_result_bridge_protocol_target_module_vis(self):
        # Arrange
        # Arrange
        data = {"x": 10, "y": 20}
        # Act
        result = add_protocol_metadata(data, "stats", "vis", "data")
        # Act
        # Assert
        # Assert
        assert result["_bridge_protocol"]["target_module"] == "vis"


    def test_extract_metadata_info_is_not_none(self):
        # Arrange
        # Arrange
        data = {
            "x": 10,
            "_bridge_protocol": {
                "bridge_protocol_version": "1.0.0",
                "source_module": "plt",
                "target_module": "vis",
                "coordinate_system": "axes",
            },
        }
        # Act
        info = extract_protocol_metadata(data)
        # Act
        # Assert
        # Assert
        assert info is not None

    def test_extract_metadata_info_source_module_equals_plt(self):
        # Arrange
        # Arrange
        data = {
            "x": 10,
            "_bridge_protocol": {
                "bridge_protocol_version": "1.0.0",
                "source_module": "plt",
                "target_module": "vis",
                "coordinate_system": "axes",
            },
        }
        # Act
        info = extract_protocol_metadata(data)
        # Act
        # Assert
        # Assert
        assert info.source_module == "plt"

    def test_extract_metadata_info_coordinate_system_equals_axes(self):
        # Arrange
        # Arrange
        data = {
            "x": 10,
            "_bridge_protocol": {
                "bridge_protocol_version": "1.0.0",
                "source_module": "plt",
                "target_module": "vis",
                "coordinate_system": "axes",
            },
        }
        # Act
        info = extract_protocol_metadata(data)
        # Act
        # Assert
        # Assert
        assert info.coordinate_system == "axes"


    def test_extract_missing_metadata(self):
        """Should return None if no metadata."""
        # Arrange
        data = {"x": 10, "y": 20}
        # Act
        info = extract_protocol_metadata(data)
        # Assert
        assert info is None


class TestCoordinateSystems:
    """Tests for coordinate system definitions."""

    def test_axes_defined_axes_in_coordinate_systems(self):
        # Arrange
        # Act
        # Assert
        # Arrange
        # Act
        # Assert
        assert "axes" in COORDINATE_SYSTEMS

    def test_axes_defined_coordinate_systems_axes_x_range_0_0_1_0(self):
        # Arrange
        # Act
        # Assert
        # Arrange
        # Act
        # Assert
        assert COORDINATE_SYSTEMS["axes"]["x_range"] == (0.0, 1.0)


    def test_data_defined_data_in_coordinate_systems(self):
        # Arrange
        # Act
        # Assert
        # Arrange
        # Act
        # Assert
        assert "data" in COORDINATE_SYSTEMS

    def test_data_defined_coordinate_systems_data_x_range_is_none(self):
        # Arrange
        # Act
        # Assert
        # Arrange
        # Act
        # Assert
        assert COORDINATE_SYSTEMS["data"]["x_range"] is None  # Depends on data


    def test_mm_defined_mm_in_coordinate_systems(self):
        """Millimeter coordinate system should be defined."""
        # Arrange
        # Act
        # Assert
        assert "mm" in COORDINATE_SYSTEMS

    def test_px_defined_px_in_coordinate_systems(self):
        """Pixel coordinate system should be defined."""
        # Arrange
        # Act
        # Assert
        assert "px" in COORDINATE_SYSTEMS


# EOF

if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.abspath(__file__)])

# --------------------------------------------------------------------------------
# Start of Source Code from: /home/ywatanabe/proj/scitex-code/src/scitex/bridge/_protocol.py
# --------------------------------------------------------------------------------
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # File: ./src/scitex/bridge/_protocol.py
# # Time-stamp: "2024-12-09 09:30:00 (ywatanabe)"
# """
# Bridge Protocol - Versioning and compatibility for cross-module communication.
#
# This module defines the bridge protocol version and provides utilities
# for ensuring compatibility between different versions of scitex modules.
#
# Protocol Versioning
# -------------------
# The bridge protocol version follows semantic versioning:
# - MAJOR: Breaking changes in bridge interfaces
# - MINOR: New bridge functions added (backward compatible)
# - PATCH: Bug fixes (backward compatible)
#
# Usage:
#     from scitex_bridge import BRIDGE_PROTOCOL_VERSION, check_protocol_compatibility
# """
#
# from typing import Dict, Any, Tuple, Optional
# from dataclasses import dataclass
#
#
# # =============================================================================
# # Protocol Version
# # =============================================================================
#
# BRIDGE_PROTOCOL_VERSION = "1.0.0"
# """
# Current bridge protocol version.
#
# Changes:
# - 1.0.0: Initial protocol
#     - Stats → Plt: add_stat_to_axes, extract_stats_from_axes
#     - Stats → Vis: stat_result_to_annotation, add_stats_to_figure_model
#     - Plt → Vis: figure_to_vis_model, axes_to_vis_axes
#     - Coordinate conventions: axes coords (0-1) for plt, data coords for vis
# """
#
#
# # =============================================================================
# # Protocol Metadata
# # =============================================================================
#
#
# @dataclass
# class ProtocolInfo:
#     """
#     Bridge protocol information for serialization and compatibility.
#
#     Parameters
#     ----------
#     version : str
#         Protocol version string (semver)
#     source_module : str
#         Module that created the data
#     target_module : str
#         Target module for the data
#     coordinate_system : str
#         Coordinate system used ("axes", "data", "figure", "mm", "px")
#     """
#
#     version: str = BRIDGE_PROTOCOL_VERSION
#     source_module: str = ""
#     target_module: str = ""
#     coordinate_system: str = "data"
#
#     def to_dict(self) -> Dict[str, Any]:
#         """Convert to dictionary."""
#         return {
#             "bridge_protocol_version": self.version,
#             "source_module": self.source_module,
#             "target_module": self.target_module,
#             "coordinate_system": self.coordinate_system,
#         }
#
#     @classmethod
#     def from_dict(cls, data: Dict[str, Any]) -> "ProtocolInfo":
#         """Create from dictionary."""
#         return cls(
#             version=data.get("bridge_protocol_version", BRIDGE_PROTOCOL_VERSION),
#             source_module=data.get("source_module", ""),
#             target_module=data.get("target_module", ""),
#             coordinate_system=data.get("coordinate_system", "data"),
#         )
#
#
# # =============================================================================
# # Compatibility Utilities
# # =============================================================================
#
#
# def parse_version(version: str) -> Tuple[int, int, int]:
#     """
#     Parse a version string into (major, minor, patch) tuple.
#
#     Parameters
#     ----------
#     version : str
#         Version string like "1.2.3"
#
#     Returns
#     -------
#     tuple
#         (major, minor, patch) integers
#     """
#     parts = version.split(".")
#     major = int(parts[0]) if len(parts) > 0 else 0
#     minor = int(parts[1]) if len(parts) > 1 else 0
#     patch = int(parts[2]) if len(parts) > 2 else 0
#     return (major, minor, patch)
#
#
# def check_protocol_compatibility(
#     data_version: str,
#     current_version: str = BRIDGE_PROTOCOL_VERSION,
# ) -> Tuple[bool, Optional[str]]:
#     """
#     Check if a data version is compatible with the current protocol.
#
#     Parameters
#     ----------
#     data_version : str
#         Version of the data being loaded
#     current_version : str
#         Current protocol version (default: BRIDGE_PROTOCOL_VERSION)
#
#     Returns
#     -------
#     tuple
#         (is_compatible, warning_message)
#         - is_compatible: True if data can be safely used
#         - warning_message: None if compatible, else a warning string
#
#     Examples
#     --------
#     >>> is_compat, msg = check_protocol_compatibility("1.0.0")
#     >>> is_compat
#     True
#
#     >>> is_compat, msg = check_protocol_compatibility("2.0.0")
#     >>> is_compat
#     False
#     >>> msg
#     'Major version mismatch: data v2.0.0, current v1.0.0'
#     """
#     data_major, data_minor, _ = parse_version(data_version)
#     curr_major, curr_minor, _ = parse_version(current_version)
#
#     # Major version mismatch = incompatible
#     if data_major != curr_major:
#         return (
#             False,
#             f"Major version mismatch: data v{data_version}, current v{current_version}",
#         )
#
#     # Minor version newer than current = warning (may have unknown fields)
#     if data_minor > curr_minor:
#         return (
#             True,
#             f"Data version newer than current: data v{data_version}, "
#             f"current v{current_version}. Some features may be ignored.",
#         )
#
#     return (True, None)
#
#
# def add_protocol_metadata(
#     data: Dict[str, Any],
#     source_module: str,
#     target_module: str,
#     coordinate_system: str = "data",
# ) -> Dict[str, Any]:
#     """
#     Add bridge protocol metadata to a dictionary.
#
#     Parameters
#     ----------
#     data : dict
#         Data dictionary to annotate
#     source_module : str
#         Source module name (e.g., "stats", "plt")
#     target_module : str
#         Target module name (e.g., "vis", "plt")
#     coordinate_system : str
#         Coordinate system used (default: "data")
#
#     Returns
#     -------
#     dict
#         Data with protocol metadata added
#
#     Examples
#     --------
#     >>> data = {"x": 10, "y": 20}
#     >>> annotated = add_protocol_metadata(data, "stats", "vis")
#     >>> annotated["_bridge_protocol"]["bridge_protocol_version"]
#     '1.0.0'
#     """
#     protocol = ProtocolInfo(
#         source_module=source_module,
#         target_module=target_module,
#         coordinate_system=coordinate_system,
#     )
#     data["_bridge_protocol"] = protocol.to_dict()
#     return data
#
#
# def extract_protocol_metadata(data: Dict[str, Any]) -> Optional[ProtocolInfo]:
#     """
#     Extract bridge protocol metadata from a dictionary.
#
#     Parameters
#     ----------
#     data : dict
#         Data dictionary that may contain protocol metadata
#
#     Returns
#     -------
#     ProtocolInfo or None
#         Protocol info if present, None otherwise
#     """
#     if "_bridge_protocol" in data:
#         return ProtocolInfo.from_dict(data["_bridge_protocol"])
#     return None
#
#
# # =============================================================================
# # Coordinate System Definitions
# # =============================================================================
#
# COORDINATE_SYSTEMS = {
#     "axes": {
#         "description": "Normalized axes coordinates (0-1)",
#         "x_range": (0.0, 1.0),
#         "y_range": (0.0, 1.0),
#         "used_by": ["plt", "matplotlib"],
#     },
#     "data": {
#         "description": "Data coordinates (actual x/y values)",
#         "x_range": None,  # Depends on data
#         "y_range": None,
#         "used_by": ["vis", "FigureModel"],
#     },
#     "figure": {
#         "description": "Figure coordinates (0-1 over entire figure)",
#         "x_range": (0.0, 1.0),
#         "y_range": (0.0, 1.0),
#         "used_by": ["matplotlib", "suptitle"],
#     },
#     "mm": {
#         "description": "Physical millimeters",
#         "x_range": None,  # Depends on figure size
#         "y_range": None,
#         "used_by": ["vis", "publication"],
#     },
#     "px": {
#         "description": "Pixels",
#         "x_range": None,  # Depends on DPI and size
#         "y_range": None,
#         "used_by": ["canvas", "gui"],
#     },
# }
#
#
# # =============================================================================
# # Public API
# # =============================================================================
#
# __all__ = [
#     "BRIDGE_PROTOCOL_VERSION",
#     "ProtocolInfo",
#     "parse_version",
#     "check_protocol_compatibility",
#     "add_protocol_metadata",
#     "extract_protocol_metadata",
#     "COORDINATE_SYSTEMS",
# ]
#
#
# # EOF

# --------------------------------------------------------------------------------
# End of Source Code from: /home/ywatanabe/proj/scitex-code/src/scitex/bridge/_protocol.py
# --------------------------------------------------------------------------------
