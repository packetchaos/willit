import pprint
import click


@click.command(help="Python Replacement for Curl")
@click.argument('url')
def api(url):
    print(url)
