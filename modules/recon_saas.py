import subprocess

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
    output = subprocess.getoutput(f"subfinder -d {domain}")
    with open("results/recon.txt", "w") as f:
        f.write(output)
    return output
