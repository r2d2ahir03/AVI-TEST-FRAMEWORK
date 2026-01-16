from framework.config_loader import load_yaml
from framework.api_client import APIClient
from framework.executor import run_parallel
from tests.test_disable_vs import disable_vs

api_cfg = load_yaml("config/api.yaml")
creds = load_yaml("config/credentials.yaml")
tests = load_yaml("config/testcases.yaml")

api = APIClient(
    api_cfg["base_url"],
    creds["username"],
    creds["password"]
)

tasks = []
for tc in tests["testcases"]:
    tasks.append(
        lambda tc=tc: disable_vs(
            api,
            api_cfg["endpoints"],
            tc["target_vs_name"]
        )
    )

run_parallel(tasks)
