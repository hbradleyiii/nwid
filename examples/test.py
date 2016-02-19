#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             app.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/06/2016
#

from __future__ import absolute_import

import curses
import nwid

app = nwid.App()

app.window = nwid.Window()
wid = nwid.widget.Base()
wid.fill = 'x'
app.window.add_child(wid)

wi = nwid.widget.Base()
wi.fill = '+'
wi.position = 25, 25
wi.string = """This is the first line.
This is the second line.
This is the  third  line.
  And <some> more...?#^$#

"""
wi.setup_buffer()
app.window.add_child(wi)

def test(_):
    wid.redraw()
    print 'whatever'
    wi.redraw()

def tst(_):
    wi.redraw()
    print 'hi there'

def clear(_):
    app.window.screen.clear()

wi.register_event(ord('r'), test)

wi.register_event(ord('a'), tst)

app.window.register_event(ord('c'), clear)

app.run()


