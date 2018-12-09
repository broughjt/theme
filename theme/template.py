import click
import os
import pystache


class Template:
    """Representation of a base16 template."""

    def __init__(self, path):
        self.path = path

    def get(self):
        """Return a parsed mustache tempate from the file specified in self.path."""
        with click.open_file(self.path, "r") as file_:
            template = pystache.parse(file_.read())
        return template

    def build(self, scheme):
        """Scheme should be a dict containing the loaded yaml scheme info."""

        built = {
            "scheme_name": scheme.pop("scheme"),
            "scheme_author": scheme.pop("author"),
            "scheme_slug": self.slug(),
        }

        for k, v in scheme.items():
            built[f"{k}-hex"] = v
            r, g, b = v[0:2], v[2:4], v[4:6]

            for kind in ["hex", "rgb", "dec"]:
                for color, number in {"r": r, "g": g, "b": b}.items():
                    if kind == "rgb":
                        number = int(number, 16)
                    elif kind == "dec":
                        number = int(number, 16) / 255

                    built[f"{k}-{kind}-{color}"] = str(number)  # Mmmmhhhhmmm oh yes

        return pystache.render(self.get(), built)

    def slug(self):
        name = os.path.basename(self.path)
        if name.endswith(".yaml"):
            name = name[:-5]
        return name.lower().replace(" ", "-")
