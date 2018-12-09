import re
import click
from theme.template import Template

NEEDLE = re.compile(r"^.*%%theme_template%%$")
END = re.compile(r"^.*%%theme_template_end%%$")


class Recipient:
    """Represents a file to inject a scheme into."""

    def __init__(self, path):
        self.path = path
        self.content = self.read()

    def inject(self, scheme):
        start = None
        lines = self.content.splitlines()
        for count, line in enumerate(lines):
            if not start:
                if NEEDLE.match(line):
                    start = count + 1
            else:
                if END.match(line):
                    end = count

        self.content = "\n".join(lines[:start] + scheme.splitlines() + lines[end:])

    def read(self):
        with click.open_file(self.path, 'r') as file_:
            return file_.read()

    def write(self):
        with click.open_file(self.path, 'w') as file_:
            file_.write(self.content)
