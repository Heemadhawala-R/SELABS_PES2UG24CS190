import pytest
from shipping_quote import process_shipments, monitor_container_pressures


def test_invalid_shipments_type():
    with pytest.raises(ValueError):
        process_shipments("invalid", 10)


def test_negative_handling_fee():
    with pytest.raises(ValueError):
        process_shipments([], -1)


def test_unapproved_shipment():
    result = process_shipments(
        [{"manifest_approved": False}], 10
    )
    assert result["status"] == "NO_CARGO"


def test_default_ground_mode():
    result = process_shipments(
        [{"manifest_approved": True,
          "packages": [{"weight_kg": 10}]}], 10
    )
    assert result["total_quote"] == 50.0
    assert result["status"] == "CLEARED"


def test_air_mode():
    result = process_shipments(
        [{"manifest_approved": True, "mode": "air",
          "packages": [{"weight_kg": 10}]}], 10
    )
    assert result["total_quote"] == 130.0


def test_unknown_mode():
    result = process_shipments(
        [{"manifest_approved": True, "mode": "sea"}], 10
    )
    assert result["status"] == "NO_CARGO"


def test_empty_packages_and_zero_quote():
    result = process_shipments(
        [{"manifest_approved": True, "packages": []}], 0
    )
    assert result == {"total_quote": 0.0, "status": "NO_CARGO"}


def test_invalid_weight():
    result = process_shipments(
        [{"manifest_approved": True,
          "packages": [{"weight_kg": 0}]}], 10
    )
    assert result["total_quote"] == 10.0
    assert result["status"] == "CLEARED"


def test_normal_weight():
    result = process_shipments(
        [{"manifest_approved": True,
          "packages": [{"weight_kg": 10}]}], 10
    )
    assert result["total_quote"] == 50.0


def test_heavy_weight():
    result = process_shipments(
        [{"manifest_approved": True,
          "packages": [{"weight_kg": 40}]}], 10
    )
    assert result["total_quote"] == 250.0


def test_hazmat_non_fragile():
    result = process_shipments(
        [{"manifest_approved": True,
          "is_fragile": False,
          "packages": [{"weight_kg": 5, "is_hazmat": True}]}], 10
    )
    assert result["total_quote"] == 60.0


def test_hazmat_fragile():
    result = process_shipments(
        [{"manifest_approved": True,
          "is_fragile": True,
          "packages": [{"weight_kg": 5, "is_hazmat": True}]}], 10
    )
    assert result["total_quote"] == 0.0
    assert result["status"] == "NO_CARGO"


def test_express_priority():
    result = process_shipments(
        [{"manifest_approved": True,
          "express_priority": True,
          "packages": [{"weight_kg": 10}]}], 10
    )
    assert result["total_quote"] == 62.5


def test_flagged_review():
    shipments = [
        {"manifest_approved": True, "mode": "sea"},
        {"manifest_approved": True, "mode": "sea"},
        {"manifest_approved": True, "mode": "sea"},
        {"manifest_approved": True, "mode": "sea"},
    ]
    result = process_shipments(shipments, 10)
    assert result["status"] == "FLAGGED_REVIEW"


def test_not_flagged_review():
    result = process_shipments(
        [{"manifest_approved": True, "mode": "sea"}], 10
    )
    assert result["status"] == "NO_CARGO"


def test_empty_pressure_logs():
    assert monitor_container_pressures([]) == "NO_DATA"


def test_stable_pressure():
    assert monitor_container_pressures([[15, 16, 17]]) == "STABLE"


def test_pressure_streak_resets():
    assert monitor_container_pressures([[13, 15, 13, 15]]) == "STABLE"


def test_leak_detected():
    assert monitor_container_pressures([[15, 13, 12]]) == "LEAK_DETECTED"
