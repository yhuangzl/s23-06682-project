"""Main entrypoint."""

import click

from .works import Works


@click.command(help="OpenAlex Institutions")
@click.argument("query", nargs=-1)
def main(query):
    """
    Main functions.
    """

    work = Works(query[0])
    return work.ris
