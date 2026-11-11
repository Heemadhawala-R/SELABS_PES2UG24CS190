
import json
import math

def calculate_dimensional_weight(dimensions_str):
    if not isinstance(dimensions_str, str):
        return None

    try:
        dims = dimensions_str.split('x')

        if len(dims) != 3:
            return None

        length = float(dims[0])
        width = float(dims[1])
        height = float(dims[2])

        if not all(math.isfinite(d) and d > 0 for d in (length, width, height)):
            return None

        return round((length * width * height) / 5000.0, 2)

    except (ValueError, TypeError):
        return None


def format_tracking_label(raw_code):
    if not isinstance(raw_code, str):
        return None

    try:
        raw_code = raw_code.strip()

        if len(raw_code) < 2:
            return None

        prefix = raw_code[0]

        if not prefix.isalpha() or not prefix.isascii():
            return None

        if not raw_code[1:].isdigit():
            return None

        tracking_num = int(raw_code[1:])

        return f"{prefix.upper()}-{tracking_num:06d}"

    except (ValueError, TypeError):
        return None


def parse_package_manifest(json_payload):
    if not isinstance(json_payload, str):
        return None

    try:
        data = json.loads(json_payload)

        if not isinstance(data, dict) or "weight" not in data:
            return None

        weight = data["weight"]

        if isinstance(weight, bool) or not isinstance(weight, (int, float)):
            return None

        weight = float(weight)

        if not math.isfinite(weight) or weight < 0:
            return None

        return weight

    except (ValueError, TypeError, OverflowError):
        return None


def main():
    print("==== Running calculate_dimensional_weight ====")
    dims_input = input("Enter dimensions LxWxH in cm (e.g. 20x30x10): ")
    dim_weight = calculate_dimensional_weight(dims_input)
    print("Dimensional Weight (kg):", dim_weight)

    print("\n==== Running format_tracking_label ====")
    code_input = input("Enter raw code (e.g. E123): ")
    label = format_tracking_label(code_input)
    print("Formatted Label:", label)

    print("\n==== Running parse_package_manifest ====")
    json_input = input('Enter manifest JSON (e.g. {"weight": 12.5}): ')
    weight = parse_package_manifest(json_input)
    print("Manifest Weight:", weight)


if __name__ == "__main__":
    main()
