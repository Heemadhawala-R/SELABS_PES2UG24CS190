
from hypothesis import given, strategies as st
from processor import calculate_dimensional_weight, format_tracking_label, parse_package_manifest

@given(st.text() | st.none())
def test_calculate_dimensional_weight_no_crash(s):
    #To-Do:Using try and except complete this function.
    try:
        calculate_dimensional_weight(s)
    except Exception as e:
        assert False, f"calculate_dimensional_weight crashed with: {e}"

@given(st.text() | st.none())
def test_format_tracking_label_safe(s):
    #To-Do:Using try and except complete this function.
    try:
        format_tracking_label(s)
    except Exception as e:
        assert False, f"format_tracking_label crashed with: {e}"

@given(st.text() | st.none())
def test_parse_package_manifest_safe(s):
    #To-Do:Using try and except complete this function.
    try:
        parse_package_manifest(s)
    except Exception as e:
        assert False, f"parse_package_manifest crashed with: {e}"
def test_valid_dimensional_weight():
    assert calculate_dimensional_weight("20x30x10") == 1.2

def test_invalid_dimensional_weight():
    assert calculate_dimensional_weight("20x30") is None
    assert calculate_dimensional_weight("-10x20x30") is None

def test_valid_tracking_label():
    assert format_tracking_label("E123") == "E-000123"

def test_invalid_tracking_label():
    assert format_tracking_label("") is None
    assert format_tracking_label("EABC") is None

def test_valid_package_manifest():
    assert parse_package_manifest('{"weight": 12}') == 12.0

def test_invalid_package_manifest():
    assert parse_package_manifest('{"price": 12}') is None
    assert parse_package_manifest('invalid json') is None