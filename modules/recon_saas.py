import subprocess
import re

def saml_enum(domain):
    try:
        output = subprocess.getoutput(f"curl -s -X POST https://{domain}/adfs/ls/")
        lines = [line for line in output.splitlines() if "saml" in line.lower()]
        with open("results/recon.txt", "w") as f:
            f.write("\n".join(lines) or "No SAML data found.")
        return lines
    except Exception as e:
        return [f"Error: {e}"]

def subdomain_enum(domain):
    import re
    def clean_html(raw):
        cleanr = re.compile("<.*?>")
        return re.sub(cleanr, "", raw)
    output = subprocess.getoutput(f"subfinder -d {domain}")
    clean_output = clean_html(output)
    clean_output = re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', output)
    with open("results/recon.txt", "w") as f:
        f.write(clean_output)
    return clean_output
