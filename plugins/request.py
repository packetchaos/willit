import requests
import click
import pprint


@click.command(help="Requests at the commandline; replacement for curl")
@click.argument("url")
@click.option("--useragent", default=None, help="Set the User Agent")
@click.option("--params", default=None, help="Set the Parameters")
@click.option("--response", required=True, type=click.Choice(['status_code', 'content', 'json', 'headers', 'cookies', 'text']))
def request(url, useragent, params, response):

    data = requests.get(url, headers=useragent, params=params)

    if response == 'status_code':
        print(data.status_code)
    elif response == 'content':
        print(data.content)
    elif response == 'json':
        pprint.pprint(data.json())
    elif response == 'headers':
        print(data.headers)
    elif response == 'cookies':
        print(data.cookies)
    elif response == 'text':
        pprint.pprint(data.text)
    else:
        print("Something went wrong")
