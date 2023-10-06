from extractor.core import get_raw_data, filter_data


def test_get_raw_data():
    response = get_raw_data("pandas")
    assert response["name"] == "pandas"


def test_log_error_on_invalid_package(capsys):
    response = get_raw_data("invalid_package")
    captured = capsys.readouterr()
    assert "ERROR" in captured.out
    assert response == {}


def test_missing_input_on_filter_data():
    filtered_data = filter_data(None, None)
    assert filtered_data == {}
