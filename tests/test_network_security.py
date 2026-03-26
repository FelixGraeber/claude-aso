import pytest

from scripts.fetch_listing import detect_platform
from scripts.network_security import validate_remote_url
from scripts.screenshot_analyzer import analyze_screenshot_url


def test_detect_platform_rejects_spoofed_store_host() -> None:
    with pytest.raises(ValueError):
        detect_platform("https://example.com/?next=https://apps.apple.com/app/id123456")


def test_validate_remote_url_blocks_private_destinations() -> None:
    with pytest.raises(ValueError):
        validate_remote_url("http://127.0.0.1:8080/internal")


def test_screenshot_analyzer_rejects_private_destinations_without_request() -> None:
    result = analyze_screenshot_url("http://127.0.0.1:8000/screenshot.png")

    assert result["accessible"] is False
    assert "private IP" in result["error"]
