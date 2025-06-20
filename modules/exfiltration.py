import requests

def trigger_webhook_exfiltration(api_url, webhook_url):
    try:
        data = {"event": "test", "status": "exfil"}
        r = requests.post(webhook_url, json=data, timeout=5)
        return f"{webhook_url} | {r.status_code}"
    except Exception as e:
        return f"Error: {e}"
