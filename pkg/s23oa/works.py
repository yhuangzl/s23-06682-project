"""Work class of openalex entity."""

# import base64
import bibtexparser
import requests

# from IPython.display import display, HTML

# import matplotlib.pyplot as plt
# from IPython.core.pylabtools import print_figure


class Works:
    """
    Work class of openalex entity.
    """

    def __init__(self, oaid):
        """
        Init funciton.
        """

        self.oaid = oaid
        self.req = requests.get(f"https://api.openalex.org/works/{oaid}")
        self.data = self.req.json()

    def __str__(self):
        """
        Str funciton.
        """

        return "str"

    @property
    def ris(self):
        """
        ris funciton.
        """

        fields = []
        if self.data["type"] == "journal-article":
            fields += ["TY  - JOUR"]
        else:
            raise Exception("Unsupported type {self.data['type']}")

        for author in self.data["authorships"]:
            fields += [f'AU  - {author["author"]["display_name"]}']

        fields += [f'PY  - {self.data["publication_year"]}']
        fields += [f'TI  - {self.data["title"]}']
        fields += [f'JO  - {self.data["host_venue"]["display_name"]}']
        fields += [f'VL  - {self.data["biblio"]["volume"]}']

        if self.data["biblio"]["issue"]:
            fields += [f'IS  - {self.data["biblio"]["issue"]}']

        fields += [f'SP  - {self.data["biblio"]["first_page"]}']
        fields += [f'EP  - {self.data["biblio"]["last_page"]}']
        fields += [f'DO  - {self.data["doi"]}']
        fields += ["ER  -"]

        ris = "\n".join(fields)
        # ris64 = base64.b64encode(ris.encode("utf-8")).decode("utf8")
        # uri = f'<pre>{ris}</pre><br><a href="data:text/plain;base64,\
        # {ris64}" download="ris">Download RIS</a>'

        # display(HTML(uri))
        print(ris)
        return ris

    @property
    def bibtex(self):
        """
        bibtex funciton.
        """

        _authors = [au["author"]["display_name"] for au in self.data["authorships"]]
        if len(_authors) == 1:
            authors = _authors[0]
        else:
            authors = ", ".join(_authors)

        article_id = _authors[0].split()[-1] + "_" + str(self.data["publication_year"])

        database = bibtexparser.bibdatabase.BibDatabase
        database.entries = [
            {
                "year": str(self.data["publication_year"]),
                "volume": self.data["biblio"]["volume"],
                "url": self.data["doi"],
                "title": self.data["title"],
                "pages": "-".join(
                    [
                        self.data["biblio"]["first_page"],
                        self.data["biblio"]["last_page"],
                    ]
                ),
                "number": self.data["biblio"]["issue"],
                "journal": self.data["host_venue"]["display_name"],
                "doi": self.data["doi"].replace("https://doi.org/", ""),
                "author": authors,
                "ENTRYTYPE": "article",
                "ID": article_id,
            }
        ]
        database.comments = []
        database.strings = {}
        database.preambles = []

        bibtex_str = bibtexparser.dumps(database)

        print(bibtex_str)
        return bibtex_str
