from enum import Enum

import typer
from typing_extensions import Annotated

from extractor.core import generate_data

app = typer.Typer()


class RequirementsFormat(str, Enum):
    pip_list = "pip_list"
    pip_freeze = "pip_freeze"


@app.command()
def main(
    source_path: Annotated[
        str, typer.Option(prompt=True, help="Requirements file path")
    ] = "",
    output: Annotated[
        str, typer.Option(prompt=True, help="Path to store the data")
    ] = "",
    format: Annotated[
        RequirementsFormat,
        typer.Option(prompt=True, help="Incoming requirements format."),
    ] = RequirementsFormat.pip_freeze,
):
    # empty_arg = ""
    # if source_path == empty_arg:
    #     source_path = typer.prompt("Source path")
    # if output == empty_arg:
    #     output = typer.prompt("Output path")
    generate_data(source_path, output, format)


# if __name__ == "__main__":
#     app()
