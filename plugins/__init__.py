from .mail import mail
from .push import push
from .ssh import ssh
from .smtp import smtp
from .mac_lookup import mac
from .sweep import scan
from .base_decode import debase
from .bs import bs
from .request import request


def plugin_loader(group):
    group.add_command(mail)
    group.add_command(push)
    group.add_command(ssh)
    group.add_command(smtp)
    group.add_command(mac)
    group.add_command(scan)
    group.add_command(debase)
    group.add_command(bs)
    group.add_command(request)
