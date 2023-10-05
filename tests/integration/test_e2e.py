import os
import shutil
from typer.testing import CliRunner

from extractor.core import extract_data, save_data

MOCKS_PATH = "tests/mocks"
INPUTS_PATH = os.path.join(MOCKS_PATH, "in")
OUTPUTS_PATH = os.path.join(MOCKS_PATH, "out")

runner = CliRunner()


def test_pip_freeze_format():
    input_format = "pip_freeze"
    source_path = os.path.join(INPUTS_PATH, input_format, "sample_1.txt")
    output_path = os.path.join(OUTPUTS_PATH, input_format, "pip_freeze_sample_1.csv")

    data = extract_data(
        source_path,
        input_format
    )

    save_data(data, output_path)

    assert os.path.exists(
        os.path.join(output_path)
    )
    assert os.stat(output_path).st_size > 0
    shutil.rmtree(OUTPUTS_PATH)


def test_pip_list_format():
    input_format = "pip_list"
    source_path = os.path.join(INPUTS_PATH, input_format, "sample_3.txt")
    output_path = os.path.join(OUTPUTS_PATH, input_format,"pip_list_sample_3.csv")

    data = extract_data(
        source_path,
        input_format
    )

    save_data(data, output_path)

    assert os.path.exists(
        os.path.join(output_path)
    )
    assert os.stat(output_path).st_size > 0
    shutil.rmtree(OUTPUTS_PATH)