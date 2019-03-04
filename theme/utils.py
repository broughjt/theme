import click
import inquirer
import yaml
import sys
import os

from pprint import pformat


def get_yaml_dict(path):
    try:
        with click.open_file(path, 'r') as yaml_file:
            yaml_dict = yaml.safe_load(yaml_file.read()) or {}
        return yaml_dict
    except FileNotFoundError:
        return {}


def check_path(path):
    return os.path.isfile(path)


def output(kind, color, string):
    prefix = '[' + click.style(kind, fg=color) + ']'
    print(prefix, string)


def info(message):
    output('info', 'green', message)


def error(message, code=1):
    output('error', 'red', message)
    sys.exit(code)


def help_(message):
    output('help', 'yellow', message)


def debug(*args):
    if click.get_current_context().obj['DEBUG']:
        string = ''

        for arg in args:
            if isinstance(arg, (list, dict)):
                output('debug', 'magenta', string + pformat(arg))
                string = ''
            else:
                string += str(arg) + ' '

        if string != '':
            output('debug', 'magenta', string)


def matching(match, collection):
    matches = []
    for item in collection:
        if match in item:
            matches.append(item)
    return matches


def narrow(matches, to, max=30):
    if len(matches) > 1:
        question = inquirer.List(
            'theme',
            message='Which one?',
            choices=matches
        )
        return inquirer.prompt([question])['theme']
    elif len(matches) == 1:
        match = matches[0]
        if match == to:
            return match
        else:
            question = inquirer.Confirm(
                'theme',
                message=f"THEME matched '{match}'. Set theme to {match}?",
                default=True
            )
            if inquirer.prompt([question])['theme']:
                return match
            else:
                sys.exit(0)
    else:
        error('Theme not found')
