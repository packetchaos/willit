from .api import api
from .mail import mail
from .push import push
from .ssh import ssh
from .smtp import smtp
from .mac_lookup import mac
from .sweep import scan


def plugin_loader(group):
    group.add_command(api)
    group.add_command(mail)
    group.add_command(push)
    group.add_command(ssh)
    group.add_command(smtp)
    group.add_command(mac)
    group.add_command(scan)
