def analyze_health(blood_values):

    import json

    import os

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(BASE_DIR, "config", "ranges.json")

    with open(config_path) as f:
        ranges = json.load(f)

    analysis = {}

    for test, value in blood_values.items():

        if test not in ranges:
            continue

        low = ranges[test]["low"]
        high = ranges[test]["high"]

        if value < low:
            status = "LOW"
            explanation = f"{test} is below normal range. Medical review recommended."

        elif value > high:
            status = "HIGH"
            explanation = f"{test} is above normal range. Possible abnormal condition."

        else:
            status = "NORMAL"
            explanation = f"{test} level is within healthy range."

        analysis[test] = {
            "value": value,
            "status": status,
            "range": f"{low}-{high}",
            "explanation": explanation
        }

    return analysis