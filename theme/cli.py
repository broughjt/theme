import appdirs
import click
import os
from pathlib import Path
from theme.grid import Grid
from theme.utils import (
    get_yaml_dict, matching, narrow, error, debug, check_path, help_
)
from theme.recipient import Recipient
from theme.template import Template

CONFIG = Path(appdirs.user_config_dir("theme", "broughjt"))
DATA = Path(appdirs.user_data_dir("theme", "broughjt"))
COLUMNS = click.get_terminal_size()[0]


def get_schemes_dict():
    schemes = {}
    for scheme in DATA.glob("schemes/*/*.y*ml"):
        schemes[scheme.stem] = str(scheme)
    return schemes


def get_schemes_name():
    schemes = []
    for scheme in DATA.glob("schemes/*/*.y*ml"):
        schemes.append(scheme.stem)
    return sorted(schemes, key=str.lower)


def ensure_dirs():
    if not CONFIG.exists():
        debug("config doesn't exist")
        CONFIG.mkdir()
    if not CONFIG.is_dir():
        debug("config isn't a dir")
        CONFIG.replace(CONFIG)
    if not DATA.exists():
        error("please call theme update")


def get_config():
    return get_yaml_dict(CONFIG / "config")


def check_config(config):
    for value in config.values():
        if isinstance(value, (list, dict)):
            return False
    return True


@click.group()
@click.pass_context
@click.option('--debug/--no-debug', default=False)
def cli(ctx, debug):
    ensure_dirs()
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug


@cli.command("set")
@click.pass_context
@click.argument("theme")
def set_(ctx, theme):
    """Set a theme."""
    schemes = get_schemes_dict()
    matches = matching(theme, schemes)
    if len(matches) > 30:
        help_('Consider setting THEME to something more specific')
        error('There were more than 30 matches')
    match = narrow(matches, theme)

    config = get_config()
    if not check_config(config):
        error('Invalid config file')

    scheme_path = schemes[match]
    scheme_dict = get_yaml_dict(scheme_path)
    for key, value in config.items():
        recipient_path = os.path.expanduser(value)
        template_group = get_yaml_dict(
            DATA.joinpath(f'templates/{key}/templates/config.yaml')
        )
        possible_templates = [template for template in template_group]
        template_path = DATA.joinpath(
            f'templates/{key}/templates',
            narrow(possible_templates, 'default') + '.mustache'
        )
        if check_path(recipient_path):
            recipient = Recipient(recipient_path)
            built = Template(template_path).build(scheme_dict, scheme_path)
            recipient.inject(built)
            recipient.write()
        else:
            error('Invalid recipient file')


@cli.command("list")
@click.option("-1", "--oneline", is_flag=True, help="display one entry per line")
def list_(oneline):
    """Lists all themes."""
    schemes = get_schemes_name()

    if oneline:
        for scheme in schemes:
            print(scheme)
    else:
        grid = Grid(schemes).fit_to(COLUMNS)
        print(grid)
