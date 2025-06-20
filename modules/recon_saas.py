import subprocess

def saml_enum(domain):
    try:
        result = subprocess.check_output(["dig", f"_saml._tcp.{domain}", "SRV"], stderr=subprocess.DEVNULL).decode()
        return result.strip().splitlines() or ["No SAML records found."]
    except Exception as e:
        return [f"Error: {e}"]
