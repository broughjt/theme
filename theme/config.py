import datetime
import os
from theme.utils import get_yaml_dict, error


class Config:
    """Representation of a theme config file."""

    def __init__(self, path):
        self.path = path
        self.content = self.get()
        self.theme = self.content.pop('theme', None)
        self.check()

    def get(self):
        return get_yaml_dict(self.path)

    def check(self):
        for template, paths in self.content.items():
            if paths is None:
                raise ConfigError('Each template should contain 1 or more paths.')
            if isinstance(paths, dict):
                raise ConfigError('Each template should contain 1 or more paths.')
            if not isinstance(paths, list):
                self.content[template] = [paths]
            print(self.content[template])
            for count, path in enumerate(paths):
                path = os.path.expanduser(path)
                self.content[template][count] = path
                if not os.path.isfile(path):
                    raise FileNotFoundError(path)

    def paths(self):
        templates = {}
        for template, paths in self.content.items():
            templates[template] = []
            for count, path in enumerate(paths):
                templates[template].append(os.path.expanduser(path))
        return templates


class ConfigError(Exception):
    def __init__(self, message):
        Exception.__init__(message)
        self.when = datetime.now()


if __name__ == '__main__':
    try:
        c = Config('/home/jackson/.config/theme/config')
        print(c.paths())
    except ConfigError as err:
        error('Invalid config file: ' + err.message)
    except FileNotFoundError as err:
        error('Invalied config file: ' + "FileNotFound '" + str(err) + "'")
