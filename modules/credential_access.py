import requests, re

def scan_js_for_keys(domain):
    try:
        r = requests.get(f"https://{domain}/main.js", timeout=10)
        keys = list(set(re.findall(r"(?i)(api_key|secret|token)[\'\"\\s:=]+[a-z0-9-_]{16,}", r.text)))
        with open("results/credential_access.txt", "w") as f:
            f.write("\\n".join(keys) if keys else "No keys found.")
        return keys
    except Exception as e:
        return [f"Error: {e}"]
