#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
nwid.event
~~~~~~~~~~

This module contains objects and data structures necessary for handling events.
"""

from __future__ import absolute_import

from .event import Event
from .keyboard import *



# TODO: This should probably be moved to the terminal module
from contextlib import contextmanager

@contextmanager
def raw_terminal():
    input = sys.stdin.fileno()
    output = sys.stdout.fileno()
    original_settings = termios.tcgetattr(fd)  # Save original settings to restore them before quitting
    try:
        tty.setraw(fd)
        yield input, output
    finally:
        # restore terminal settings. Do this when all output is
        # finished - TCSADRAIN flag
        termios.tcsetattr(fd, termios.TCSADRAIN, original_settings)
