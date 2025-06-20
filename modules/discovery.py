import requests

def basic_discovery(domain):
    paths = ["admin", "login", "dashboard"]
    found = []
    for path in paths:
        try:
            r = requests.get(f"https://{domain}/{path}", timeout=3)
            if r.status_code < 400:
                found.append(f"{path} - {r.status_code}")
        except:
            continue
    with open("results/discovery.txt", "w") as f:
        f.write("\n".join(found) if found else "No paths found.")
    return found

def email_enum(domain, wordlist_path):
    try:
        with open(wordlist_path, 'r') as f:
            words = f.read().splitlines()
        found = [f"{word}@{domain}" for word in words if "admin" in word.lower()]
        with open("results/email_enum.txt", "w") as f:
            f.write("\n".join(found) if found else "No emails found.")
        return found
    except Exception as e:
        return [f"Error: {e}"]
