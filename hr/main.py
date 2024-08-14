from typing import Annotated

import typer

import hr

app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    context_settings={"terminal_width": 100},
)


@app.callback(invoke_without_command=True)
def callback(
    *,
    show_version: Annotated[bool, typer.Option(
        "--version",
        help="Show version and exit.",
        show_default=False,
        is_eager=True,
    )] = False,
) -> None:
    """
    Print horizontal rules.
    """
    if show_version:
        show_package_version()
        return None
    return None


@app.command("version")
def show_package_version() -> None:
    """
    Show the installed version of this package.
    """
    print(hr.__version__)
    return None
