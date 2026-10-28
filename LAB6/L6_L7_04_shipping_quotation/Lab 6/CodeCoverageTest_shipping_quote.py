import pytest
from shipping_quote import process_shipments, monitor_container_pressures


def test_invalid_inputs():
    with pytest.raises(ValueError):
        process_shipments("invalid", 10)

    with pytest.raises(ValueError):
        process_shipments([], -1)


def test_unapproved_shipment():
    result = process_shipments(
        [{"manifest_approved": False}], 10
    )
    assert result["status"] == "NO_CARGO"


def test_air_shipment():
    result = process_shipments(
        [{
            "manifest_approved": True,
            "mode": "air",
            "packages": [{"weight_kg": 10}]
        }],
        20
    )
    assert result["total_quote"] == 140.0
    assert result["status"] == "CLEARED"


def test_unknown_transport_mode():
    result = process_shipments(
        [{"manifest_approved": True, "mode": "sea"}], 10
    )
    assert result["status"] == "NO_CARGO"


def test_invalid_package_weight():
    result = process_shipments(
        [{
            "manifest_approved": True,
            "packages": [{"weight_kg": 0}]
        }],
        10
    )
    assert result["total_quote"] == 10.0
    assert result["status"] == "CLEARED"


def test_hazmat_non_fragile():
    result = process_shipments(
        [{
            "manifest_approved": True,
            "packages": [{"weight_kg": 5, "is_hazmat": True}]
        }],
        10
    )
    assert result["total_quote"] == 60.0
    assert result["status"] == "CLEARED"


def test_hazmat_fragile():
    result = process_shipments(
        [{
            "manifest_approved": True,
            "is_fragile": True,
            "packages": [{"weight_kg": 5, "is_hazmat": True}]
        }],
        10
    )
    assert result["status"] == "NO_CARGO"


def test_heavy_package():
    result = process_shipments(
        [{
            "manifest_approved": True,
            "packages": [{"weight_kg": 40}]
        }],
        10
    )
    assert result["total_quote"] == 250.0
    assert result["status"] == "CLEARED"


def test_express_priority():
    result = process_shipments(
        [{
            "manifest_approved": True,
            "express_priority": True,
            "packages": [{"weight_kg": 10}]
        }],
        20
    )
    assert result["total_quote"] == 75.0


def test_flagged_review():
    shipments = [
        {"manifest_approved": True, "mode": "sea"},
        {"manifest_approved": True, "mode": "sea"},
        {"manifest_approved": True, "mode": "sea"},
        {"manifest_approved": True, "mode": "sea"},
    ]
    result = process_shipments(shipments, 10)
    assert result["status"] == "FLAGGED_REVIEW"


def test_empty_pressure_logs():
    assert monitor_container_pressures([]) == "NO_DATA"


def test_leak_detected():
    assert monitor_container_pressures([[15, 13, 12]]) == "LEAK_DETECTED"


def test_stable_pressure():
    assert monitor_container_pressures([[15, 13, 14, 12, 15]]) == "STABLE"

