#!/usr/bin/env python3
# encoding: utf-8

import subprocess
import urllib

from gi.repository import Nautilus, GObject

programName = "easyshare"

class columnExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    def menu_activate_cb(self, menu, file):
        uri = file.get_uri()
        if not uri.startswith("file://"):
            return
        fileName = uri.split(r"file://")[1]
        fileName = urllib.url2pathname(fileName)
        subprocess.Popen([programName, fileName])

    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        file = files[0]

        item = Nautilus.MenuItem(
                name = "SimpleMenuExtension::Show_File_Name",
                label = "easyshare"
            )

        item.connect("activate", self.menu_activate_cb, file)

        return [item]
