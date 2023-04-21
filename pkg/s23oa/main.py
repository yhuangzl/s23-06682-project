"""Main entrypoint."""

import click

from .works import Works


@click.command(help="OpenAlex Institutions")
@click.option("--form", default="ris", help="ris or bibtex")
@click.argument("query", nargs=-1)
def main(form, query):
    """
    Main functions.
    """

    work = Works(query[0])
    if form == "ris":
        print(work.ris)
    elif form == "bibtex":
        print(work.bibtex)
    else:
        print("format error")
