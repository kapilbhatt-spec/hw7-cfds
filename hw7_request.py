"""Send input_example.json to the prediction API and print the result."""

import json
from pathlib import Path

import requests

url = "http://127.0.0.1:8000/predict"
input_path = Path(__file__).resolve().parent / "input_example.json"

try:
    with open(input_path, encoding="utf-8") as input_file:
        payload = json.load(input_file)

    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()
    result = response.json()
    print("Prediction:", result["prediction"])
    print(f"Probability of diabetes: {result['probability']:.2f}")

except requests.exceptions.ConnectionError:
    print("Could not connect. Is API working?")
except requests.exceptions.Timeout:
    print("The request timed out.")
except requests.exceptions.HTTPError as exc:
    print(f"API returned an error: {exc}")
    print("Response:", response.text)
except requests.exceptions.RequestException as exc:
    print(f"Request failed: {exc}")
except (OSError, json.JSONDecodeError) as exc:
    print(f"Could not read the input JSON: {exc}")
except (KeyError, ValueError) as exc:
    print(f"Unexpected API response: {exc}")
