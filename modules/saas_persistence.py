import requests

def use_api_key(endpoint, api_key):
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        r = requests.get(endpoint, headers=headers, timeout=5)
        return [f"Status: {r.status_code}", r.text[:200]]
    except Exception as e:
        return [f"Error: {e}"]
