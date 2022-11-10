from bs4 import BeautifulSoup
import requests
import click


def bs(url, html_object):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    click.echo(soup.findAll(html_object))


bs("https://www.cnn.com", "href")
