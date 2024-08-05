#!/usr/bin/env python3

import sys
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2

class WebView(Gtk.Window):
    def __init__(self, url):
        Gtk.Window.__init__(self, title="Webview")
        self.set_default_size(800, 600)
        self.webview = WebKit2.WebView()
        self.webview.load_uri(url)
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(self.webview)
        self.add(scrolled_window)
        self.connect("destroy", Gtk.main_quit)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: main.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    window = WebView(url)
    window.show_all()
    Gtk.main()
