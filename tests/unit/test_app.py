from typer.testing import CliRunner

from extractor.main import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
