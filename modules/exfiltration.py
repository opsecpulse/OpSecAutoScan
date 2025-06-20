import requests

def trigger_webhook_exfiltration(api_url, webhook_url):
    try:
        data = {"event": "test", "status": "exfil"}
        r = requests.post(webhook_url, json=data, timeout=5)
        output = f"{webhook_url} | {r.status_code}"
        with open("results/exfiltration.txt", "w") as f:
            f.write(output)
        return output
    except Exception as e:
        return f"Error: {e}"
