import click
from .plugins import plugin_loader


@click.group(help="A Command-line tool for the hacker in us all")
@click.pass_context
def cli(ctx):
    pass


plugin_loader(cli)
