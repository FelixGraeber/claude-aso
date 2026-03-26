import importlib.util
import os
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_apptweak_client_does_not_read_cwd_dotenv(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    module = load_module(ROOT / "extensions" / "apptweak" / "scripts" / "apptweak_client.py", "apptweak_client")
    monkeypatch.chdir(tmp_path)
    (tmp_path / ".env").write_text("APPTWEAK_API_KEY=from-cwd\n")
    monkeypatch.delenv("APPTWEAK_API_KEY", raising=False)
    monkeypatch.delenv("ASO_ENV_FILE", raising=False)

    with pytest.raises(ValueError):
        module.load_api_key()


def test_asc_client_reads_explicit_env_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    module = load_module(ROOT / "extensions" / "app-store-connect" / "scripts" / "asc_client.py", "asc_client")
    env_file = tmp_path / "aso.env"
    env_file.write_text(
        "ASC_KEY_ID=test-key\n"
        "ASC_ISSUER_ID=test-issuer\n"
        "ASC_KEY_PATH=/tmp/AuthKey_TEST.p8\n"
    )
    monkeypatch.delenv("ASC_KEY_ID", raising=False)
    monkeypatch.delenv("ASC_ISSUER_ID", raising=False)
    monkeypatch.delenv("ASC_KEY_PATH", raising=False)
    monkeypatch.setenv("ASO_ENV_FILE", os.fspath(env_file))

    creds = module.load_credentials()

    assert creds["key_id"] == "test-key"
    assert creds["issuer_id"] == "test-issuer"
    assert creds["key_path"] == "/tmp/AuthKey_TEST.p8"
