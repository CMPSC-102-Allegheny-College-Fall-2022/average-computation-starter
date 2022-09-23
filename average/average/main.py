"""Perform average computation for numbers in a single input file."""

from rich.console import Console

from pathlib import Path

import typer

# create a Typer object to support the command-line interface
cli = typer.Typer()


def confirm_valid_file(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # determine if the file is not None and if it is a file
    if file is not None:
        # the file is valid
        if file.is_file():
            return True
    # the file was either none or not valid
    return False


def compute_average(contents: str) -> float:
    """Compute the average for the numbers provided in the textual listing."""
    # TODO: initialize the count to zero
    # TODO: initialize the running total to zero
    # TODO: iterate through each line in the provided text
    # --> TODO: extract the number as an int
    # --> TODO: increment the running count
    # --> TODO: add the number to the running total
    # TODO: if there were no numbers then return -1 to indicate
    # that an average computation was not performed for them
    # TODO: if there were at least some numbers and it was acceptable
    # to perform the arithmetic mean computation for the values, return it
    return 0


@cli.command()
def average(
    dir: Path = typer.Option(None),
    file: Path = typer.Option(None),
) -> None:
    """Process a file by computing the average of all the numbers."""
    # TODO: create a console for rich text output
    # TODO: create the full name of the file
    # TODO: display a message to explain the file that will be input
    # TODO: the file is valid and so the program should compute the average of its numbers
    # --> TODO: read in the contents of the file
    # --> TODO: compute the average of all the numbers inside of the file
    # --> TODO: display all of the output in a fashion that fits the expected output,
    # making sure to include the computed average value of the numbers in the file
    # the file was not valid and thus you cannot install it
    # --> TODO: indicate in the console that the provided file was not valid
