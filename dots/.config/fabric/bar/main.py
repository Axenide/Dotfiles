#!/usr/bin/python
"""
┌──────────────────────────────────┐
│                                  │
│     ░█▀▀░█▀█░█▀▄░█▀▄░▀█▀░█▀▀     │
│     ░█▀▀░█▀█░█▀▄░█▀▄░░█░░█░░     │
│     ░▀░░░▀░▀░▀▀░░▀░▀░▀▀▀░▀▀▀     │
│                                  │
└──────────────────────────────────┘
"""
from __init__ import *

if __name__ == "__main__":
    bar = Bar()
    # osd = OSD()
    setproctitle.setproctitle("ax-bar")
    set_stylesheet_from_file(get_relative_path("style.css"))
    fabric.start()
