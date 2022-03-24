import socket
import click


def banner(ip_address, port):
    try:
        socket.setdefaulttimeout(2)
        soc = socket.socket()
        soc.connect((ip_address, int(port)))

        banner_grab = soc.recv(1024)
        click.echo("\n{} : {}".format(port, banner_grab))

    except socket.timeout:
        pass
    except ConnectionRefusedError:
        pass
    except OSError:
        pass


@click.command()
@click.argument('ip_addr')
def scan(ip_addr):
    click.echo(ip_addr)
    for ports in range(1, 65535):
        banner(ip_addr, int(ports))
