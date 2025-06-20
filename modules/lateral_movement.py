import requests

def abuse_oauth_integration(endpoint, token):
    try:
        headers = {"Authorization": f"Bearer {token}"}
        r = requests.get(endpoint, headers=headers, timeout=5)
        return f"{endpoint} | {r.status_code}"
    except Exception as e:
        return f"Error: {e}"
