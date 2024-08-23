from typing import Annotated

import typer

import hr
import hr.lib

app = typer.Typer(
    add_completion=False,
    context_settings={"terminal_width": 100},
)


@app.callback(invoke_without_command=True)
def callback(
    *,
    title: Annotated[str, typer.Argument(
        help="An optional title."
    )] = "",
    length: Annotated[int, typer.Option(
        "-l", "--length",
        help="Minimum character length.",
    )] = 50,
    border: Annotated[str, typer.Option(
        "-b", "--border",
        help="Character(s) to use for outer borders.",
    )] = "#",
    filler: Annotated[str, typer.Option(
        "-f", "--filler",
        help="Character to use for inner fillers.",
    )] = "-",
    as_paragraph: Annotated[bool, typer.Option(
        "-p", "--paragraph",
        help="Prepend 'BEGIN' and 'END' before title.",
    )] = False,
    upper: Annotated[bool, typer.Option(
        "-u", "--upper",
        help="Convert title to uppercase.",
    )] = False,
    no_newline: Annotated[bool, typer.Option(
        "-n", "--no-newline",
        help="Do not print a new-line character at the end.",
    )] = False,
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
        print(hr.__version__)
        return None

    if upper:
        title = title.upper()

    titles: list[str] = []
    if as_paragraph:
        if not title:
            titles.append("BEGIN")
            titles.append("END")
        else:
            titles.append(f"BEGIN {title}")
            titles.append(f"END {title}")
    else:
        titles.append(title)

    for title in titles:
        horizontal_rule = hr.lib.get_horizontal_rule(
            title,
            length=length,
            border=border,
            filler=filler[0],
        )
        print(horizontal_rule, end="" if no_newline else "\n")
    return None
