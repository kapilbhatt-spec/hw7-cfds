import json

import requests

url = "http://127.0.0.1:8000/predict"
try:
    with open("model.json", encoding="utf-8") as input_file:
        payload = json.load(input_file)

    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()
    print("Prediction:", response.json()["prediction"])

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
