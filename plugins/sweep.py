import socket
import click
import threading
from queue import Queue
from .request import request


lock = threading.Lock()

q = Queue()


def worker():
    # The worker thread pulls an item from the queue and processes it
    while True:
        item = q.get()
        banner(item[0], item[1])
        q.task_done()


def banner(ip_address, port):
    socket.setdefaulttimeout(2)
    soc = socket.socket()
    try:
        soc.connect((ip_address, int(port)))
        click.echo("\nPort: {} is Open.. Attempting Banner Grab\n".format(port))

        banner_grab = soc.recv(1024)
        click.echo("Port: {}... Banner: {}".format(port, banner_grab))

    except socket.timeout:
        pass
    except ConnectionRefusedError:
        pass
    except OSError:
        pass


@click.command(help='A simple ping sweep with a banner grab')
@click.argument('ip_addr')
@click.option('--port', default=None, help="Grab a banner from a particular Port")
@click.option('--start', default=1, help="Start of the port range")
@click.option('--end', default=1024, help="End of the port range")
def scan(ip_addr, port, start, end):
    ports = []
    if port:
        click.echo("\nPerforming a Banner grab on : {} over port {}".format(ip_addr, port))
        banner(ip_addr, int(port))
    else:
        click.echo("\nPerforming a Banner grab on : {} over the port range {}:{}".format(ip_addr, start, end))

        for port in range(start, end, 1):
            ports.append((ip_addr, port))

        for i in range(1000):
            t = threading.Thread(target=worker)
            t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
            t.start()

        # stuff work items on the queue (in this case, just a number).
        # start = time.perf_counter()
        for item in range(len(ports)):
            q.put(ports[item])

        q.join()
