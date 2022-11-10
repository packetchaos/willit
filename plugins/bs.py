from bs4 import BeautifulSoup
import click
import requests
import pprint


@click.command(help="Parse a Site")
@click.argument('url')
@click.argument('html_object')
@click.option('--params', default={}, help="HTML Params")
def bs(url, html_object, params):
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')

    pprint.pprint(soup.findAll(html_object))


