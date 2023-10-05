#!/usr/python3

from fabric.api import local
import os
from datetime import datetime

"""generates a .tgx file"""


def do_pack():
    """generates a .tgx file"""
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
