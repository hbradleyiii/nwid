#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             screen.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       05/31/2017
#

"""
nwid.terminal.screen
~~~~~~~~~~~~~~~~~~~~

This module contains functions responsible for clearing the screen and getting
its size.
"""

from __future__ import absolute_import

from .codes import *


def size():
    """Returns the size of the window as a tuple of columns, rows. (x, y)
    Note that this is the actual size; in order to get the bottom right corner,
    you must subtract 1 from both the rows and the columns."""
    try:
        from struct import unpack
        from fcntl import ioctl
        from termios import TIOCGWINSZ
        from os import ctermid

        with open(ctermid()) as fd:
            size = unpack('hh', ioctl(fd, TIOCGWINSZ, '----'))
            return (size[1], size[0])  # swap the size so we have (x, y)

    except ImportError:
        from os import environ
        try:
            return (environ['COLUMNS'], environ['LINES'])
        except KeyError:
            return (25, 80)  # just send back a best guess

def clear():
    """Clears the entire screen."""
    CLEAR_SCREEN.execute()

def clear_down():
    """Clears the screen from the cursor down."""
    CLEAR_DOWN.execute()

def clear_up():
    """Clears the screen from the cursor down."""
    CLEAR_UP.execute()

def clear_line():
    """Clears the entire line."""
    CLEAR_LINE.execute()

def clear_line_forward():
    """Clears the line from the cursor forward."""
    # TODO: inclusive or exclusive?
    CLEAR_LINE_FORWARD.execute()

def clear_line_backward():
    """Clears the line from the cursor backward."""
    # TODO: inclusive or exclusive?
    CLEAR_LINE_BACKWARD.execute()

def reset():
    """Clears the entire screen and places cursor at top left corner."""
    CLEAR_SCREEN.execute()
    CURSOR_SET_POSITION.execute(0, 0)