import base64
import click


def decode_base_64(base64string):
    return base64.b64decode(base64string)


@click.command(help="Decode Base64 encoding")
@click.argument('user_string')
def debase(user_string):
    print("\n{}\n".format(decode_base_64(user_string)))
