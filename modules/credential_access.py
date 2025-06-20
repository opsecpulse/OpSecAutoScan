import requests, re

def scan_js_for_keys(domain):
    try:
        r = requests.get(f"https://{domain}/main.js", timeout=5)
        return list(set(re.findall(r"(?i)(api_key|secret|token)[\'\"\\s:=]+[a-z0-9-_]{16,}", r.text)))
    except Exception as e:
        return [f"Error: {e}"]
