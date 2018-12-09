import click
import yaml


def get_yaml_dict(path):
    try:
        with click.open_file(path, "r") as yaml_file:
            yaml_dict = yaml.safe_load(yaml_file.read()) or {}
        return yaml_dict
    except FileNotFoundError:
        return {}
