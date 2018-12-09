import click
import glob
import sys
from pathlib import Path
from theme.utils import get_yaml_dict
from theme.recipient import Recipient
from theme.template import Template


@click.group()
def cli():
    pass


@cli.command()
@click.argument('theme')
def set(theme):
    """Set a theme."""
    config = get_yaml_dict('/home/jackson/.config/theme/config.yml')
    base_dir = Path('/home/jackson/colors')
    schemes = [scheme.name.replace(scheme.suffix, '') for scheme in base_dir.glob('schemes/*/*.y*ml')]
    scheme = []

    for i in schemes:
        if theme in i:
            scheme.append(i)

    if len(scheme) > 1:
        print('Which one?')
        for i, poop in enumerate(scheme):
            print(f'  {i} {poop}')
        scheme = scheme[int(input(f'{[x for x in range(len(scheme))]}: '))]
    elif len(scheme) == 1:
        scheme = schemes[0]
    else:
        print('error: theme not found.')
        sys.exit(1)

    # scheme_dict = get_yaml_dict(scheme)

    # for k, v in config.items():
    #     print(f'setting {k} to {theme} in {v}')
    #     recipient = Recipient(v)
    #     template = Template(f'/home/jackson/colors/templates/{k}/templates/default.mustache')
    #     built = template.build(scheme_dict)
    #     recipient.inject(built)
    #     recipient.write()


@cli.command()
def list():
    """Lists all themes."""
    schemes = Path('/home/jackson/colors/schemes')
    for i in schemes.iterdir():
        if i.is_dir():
            print(i)
