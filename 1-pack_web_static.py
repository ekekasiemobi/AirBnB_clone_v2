#!/usr/python3

from fabric.api import local
import os
from datetime import datetime


def do_pack():
    try:
        now = datetime.now()
        path = "web_static_{}.tgz".format(
            now.strftime("%Y%m%d%H%M%S")
        )
        local("mkdir versions")
        output = local("tar -cvzf {} web_static".format(path))
        return output
    except Exception as e:
        return None
