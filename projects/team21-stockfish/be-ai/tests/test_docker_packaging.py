from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_dockerfile_uses_locked_uv_environment_for_fastapi() -> None:
    dockerfile = (ROOT / "Dockerfile").read_text()

    assert "ghcr.io/astral-sh/uv:python3.14" in dockerfile
    assert "uv sync --locked --no-install-project" in dockerfile
    assert 'CMD ["uvicorn", "app.main:app"' in dockerfile


def test_compose_runs_collection_before_api_on_persistent_volume() -> None:
    compose = yaml.safe_load((ROOT / "compose.yaml").read_text())
    services = compose["services"]

    assert "be_ai_data" in compose["volumes"]
    assert services["collector"]["command"] == [
        "python",
        "-m",
        "app.ingestion.manual_collect",
    ]
    assert services["collector"]["restart"] == "no"
    assert services["api"]["depends_on"]["collector"]["condition"] == (
        "service_completed_successfully"
    )

    for service_name in ("collector", "api"):
        service = services[service_name]
        assert service["env_file"] == [".env"]
        assert "be_ai_data:/app/data" in service["volumes"]


def test_dockerignore_excludes_local_state_and_secrets() -> None:
    dockerignore = {
        line.strip()
        for line in (ROOT / ".dockerignore").read_text().splitlines()
        if line.strip() and not line.startswith("#")
    }

    assert ".env" in dockerignore
    assert ".venv" in dockerignore
    assert "data/" in dockerignore
    assert "__pycache__/" in dockerignore
