import os
import shutil
import tempfile

from extractor.core import extract_data, save_data

MOCKS_PATH = "tests/mocks"
INPUTS_PATH = os.path.join(MOCKS_PATH, "in")
OUTPUTS_PATH = tempfile.mkdtemp(dir=".")
SAMPLE_1 = os.path.join(INPUTS_PATH, "pip_freeze", "sample_1.txt")
SAMPLE_2 = os.path.join(INPUTS_PATH, "pip_freeze", "sample_2.txt")
SAMPLE_3 = os.path.join(INPUTS_PATH, "sample_3.txt")


def test_main_components():
    input_format = "pip_freeze"
    source_path = os.path.join(INPUTS_PATH, input_format)
    output_path = os.path.join(OUTPUTS_PATH, "pip_freeze_output.csv")

    data = extract_data(source_path, input_format)

    save_data(data, output_path)

    assert os.path.exists(os.path.join(output_path))
    assert os.stat(output_path).st_size > 0
    shutil.rmtree(OUTPUTS_PATH)


def test_pip_list_format():
    input_format = "pip_list"
    output_path = os.path.join(OUTPUTS_PATH, "output_3.csv")

    data = extract_data(SAMPLE_3, input_format)
    save_data(data, output_path)

    assert os.path.exists(os.path.join(output_path))
    assert os.stat(output_path).st_size > 0
    assert output_path.endswith(".csv")

    shutil.rmtree(OUTPUTS_PATH)


def test_save_xlsx():
    input_format = "pip_list"
    source_path = os.path.join(INPUTS_PATH, "sample_3.txt")
    output_path = os.path.join(OUTPUTS_PATH, "output_3.xlsx")

    data = extract_data(source_path, input_format)
    save_data(data, output_path)

    assert os.path.exists(os.path.join(output_path))
    assert os.stat(output_path).st_size > 0
    assert output_path.endswith(".xlsx")

    shutil.rmtree(OUTPUTS_PATH)
