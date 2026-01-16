from framework.mock_connectors import mock_ssh, mock_rdp
from framework.validations import validate_enabled

def disable_vs(api, endpoints, target_vs_name):

    print("=== PRE-FETCHER ===")
    tenants = api.get(endpoints["tenants"])
    vss = api.get(endpoints["virtualservices"])
    ses = api.get(endpoints["serviceengines"])

    print(f"Tenants: {len(tenants.get('results', []))}")
    print(f"VS: {len(vss.get('results', []))}")
    print(f"SE: {len(ses.get('results', []))}")

    print("=== PRE-VALIDATION ===")
    vs = next(v for v in vss["results"] if v["name"] == target_vs_name)
    vs_uuid = vs["uuid"]

    vs_details = api.get(f"{endpoints['virtualservices']}/{vs_uuid}")
    validate_enabled(vs_details, True)

    mock_ssh("controller")
    mock_rdp("windows-host")

    print("=== TASK ===")
    api.put(
        f"{endpoints['virtualservices']}/{vs_uuid}",
        {"enabled": False}
    )

    print("=== POST-VALIDATION ===")
    updated = api.get(f"{endpoints['virtualservices']}/{vs_uuid}")
    validate_enabled(updated, False)

    print("TEST PASSED")
