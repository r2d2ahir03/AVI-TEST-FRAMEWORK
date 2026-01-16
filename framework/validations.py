def validate_enabled(vs, expected):
    if vs.get("enabled") != expected:
        raise Exception(
            f"Expected enabled={expected}, got {vs.get('enabled')}"
        )
