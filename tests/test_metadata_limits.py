from scripts.validate_metadata import validate_metadata


def test_android_title_limit_is_thirty_characters() -> None:
    report = validate_metadata(
        "android",
        {
            "title": "x" * 31,
            "short_description": "Short description",
            "full_description": "Useful description",
        },
    )

    assert report["overall_pass"] is False
    assert report["fields"]["title"]["limit"] == 30
    assert any(issue["field"] == "title" for issue in report["issues"])


def test_android_title_within_limit_passes() -> None:
    report = validate_metadata(
        "android",
        {
            "title": "x" * 30,
            "short_description": "Short description",
            "full_description": "Useful description",
        },
    )

    assert report["fields"]["title"]["pass"] is True
