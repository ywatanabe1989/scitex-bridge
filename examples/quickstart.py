"""scitex-bridge quickstart: cross-module protocol metadata helpers.

scitex-bridge connects stats / plt / vis modules. Its protocol-versioning
helpers are pure (no heavy deps), so we exercise those for the smoke test.
"""

import scitex_bridge


def main():
    print("BRIDGE_PROTOCOL_VERSION =", scitex_bridge.BRIDGE_PROTOCOL_VERSION)
    assert scitex_bridge.BRIDGE_PROTOCOL_VERSION  # non-empty string

    # 1. check_protocol_compatibility: same version is compatible.
    ok, warn = scitex_bridge.check_protocol_compatibility(
        scitex_bridge.BRIDGE_PROTOCOL_VERSION
    )
    print("\nsame-version compat:", ok, "| warn:", warn)
    assert ok is True
    assert warn is None

    # 2. Older minor version: still compatible (typically with a warning).
    ok2, warn2 = scitex_bridge.check_protocol_compatibility("1.0.0")
    print("older-version compat:", ok2, "| warn:", warn2)

    # 3. add_protocol_metadata + extract_protocol_metadata round-trip.
    payload = {"data": [1, 2, 3], "label": "demo"}
    stamped = scitex_bridge.add_protocol_metadata(
        payload, source_module="stats", target_module="plt"
    )
    print("\nstamped payload keys:", list(stamped.keys()))
    info = scitex_bridge.extract_protocol_metadata(stamped)
    print("extracted ProtocolInfo:", info)
    assert info is not None

    # 4. Inspect coordinate conventions for plt vs vis bridges.
    print("\nCOORDINATE_SYSTEMS =", scitex_bridge.COORDINATE_SYSTEMS)
    assert isinstance(scitex_bridge.COORDINATE_SYSTEMS, dict)


if __name__ == "__main__":
    main()
