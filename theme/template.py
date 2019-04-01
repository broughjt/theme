import click
import os
import pystache


class Template:
    """Representation of a base16 template."""

    def __init__(self, path):
        self.path = path

    def get(self):
        """Return a mustache tempate from the file specified in self.path."""
        with click.open_file(self.path, "r") as file_:
            template_dict = file_.read()
        return template_dict

    def build(self, scheme_dict, scheme_file):
        """Scheme should be a dict containing the loaded yaml scheme info."""
        bases = scheme_dict.copy()

        print(bases)
        built = {
            "scheme-name": bases.pop("scheme"),
            "scheme-author": bases.pop("author"),
            "scheme-slug": slug(scheme_file),
        }

        for key, value in bases.items():
            built[f"{key}-hex"] = value
            r, g, b = value[0:2], value[2:4], value[4:6]

            for kind in ["hex", "rgb", "dec"]:
                for color, number in {"r": r, "g": g, "b": b}.items():
                    if kind == "rgb":
                        number = int(number, 16)
                    elif kind == "dec":
                        number = int(number, 16) / 255
                    built[f"{key}-{kind}-{color}"] = str(number)

        print(built)

        return pystache.render(self.get(), built)


def slug(scheme_file):
    name = os.path.basename(scheme_file)
    if name.endswith(".yaml"):
        name = name[:-5]
    elif name.endswith(".yml"):
        name = name[:-4]
    return name.lower().replace(" ", "-")
