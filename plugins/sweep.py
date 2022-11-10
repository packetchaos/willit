import socket
import click
import threading
from queue import Queue


lock = threading.Lock()

q = Queue()


def worker():
    # The worker thread pulls an item from the queue and processes it
    while True:
        item = q.get()
        banner(item[0], item[1])
        q.task_done()


def banner(ip_address, port):
    try:
        socket.setdefaulttimeout(2)
        soc = socket.socket()
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


@click.command()
@click.argument('ip_addr')
@click.option('--port', default=None, help="Grab a banner from a particular Port")
def scan(ip_addr, port):
    ports = []
    if port:
        click.echo("Performing a Banner grab on : {} over port {}".format(ip_addr, port))
        banner(ip_addr, int(port))
    else:
        click.echo("Performing a Banner grab on : {} over the first 1024 ports".format(ip_addr))

        for port in range(1025):
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
