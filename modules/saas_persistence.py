import requests

def use_api_key(endpoint, api_key):
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        r = requests.get(endpoint, headers=headers, timeout=5)
        output = f"Status: {r.status_code}\n{r.text[:200]}"
        with open("results/saas_persistence.txt", "w") as f:
            f.write(output)
        return [output]
    except Exception as e:
        return [f"Error: {e}"]
