import requests

def abuse_oauth_integration(endpoint, token):
    try:
        headers = {"Authorization": f"Bearer {token}"}
        r = requests.get(endpoint, headers=headers, timeout=5)
        output = f"{endpoint} | {r.status_code}"
        with open("results/lateral_movement.txt", "w") as f:
            f.write(output)
        return output
    except Exception as e:
        return f"Error: {e}"
