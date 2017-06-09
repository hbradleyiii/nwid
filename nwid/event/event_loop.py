#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             event_loop.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       06/07/2017
#

"""
nwid.event.event_loop
~~~~~~~~~~~~~~~~~~~~~

This module contains the mixin for an object that has an EventLoop.
"""

from __future__ import absolute_import

import os


class EventLoop(EventHandler):
    """A mixin for an EventHandler object that has an event loop (an application object)."""
    def event_loop(self):
        while True:
            try:
                keyboard_input = self.getch()
                event = Event(keyboard_input, cursor_pos)
                self.handle(event)

            except PreventDefault:
                """Continue looping. Break out of the event propagation."""
                continue

    def getch(self):
        """Gets a single character from input."""
        return os.read(sys.stdin.fileno(), 4)
