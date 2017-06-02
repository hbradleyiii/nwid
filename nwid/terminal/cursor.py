#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             cursor.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       05/30/2017
#

"""
nwid.terminal.cursor
~~~~~~~~~~~~~~~~~~~~

This module contains functions responsible for moving and manipulating the
cursor.
"""

from __future__ import absolute_import

from .codes import *


def hide():
    """Hides the cursor."""
    CURSOR_HIDE.execute()

def show():
    """Shows the cursor."""
    CURSOR_SHOW.execute()

def move_up(n=1):
    """Moves your cursor up 'n' rows."""
    # TODO: is math correct here ?
    CURSOR_UP.execute(n)

def move_down(n=1):
    """Moves your cursor down 'n' rows."""
    CURSOR_DOWN.execute(n)

def move_left(n=1):
    """Moves your cursor left (backward) 'n' characters."""
    CURSOR_LEFT.execute(n)

def move_right(n=1):
    """Moves your cursor right (forward) 'n' characters."""
    CURSOR_RIGHT.execute(n)
    pass

def next_line(n=1):
    """Moves your cursor (up) to the start of the next 'n'th line."""
    CURSOR_NEXT_LINE.execute(n)

def previous_line(n=1):
    """Moves your cursor (down) to the start of the previous 'n'th line."""
    CURSOR_PREVIOUS_LINE.execute(n)

def horizontal_absolute(n=1):
    """Moves your cursor to the 'n' column."""
    # TODO: not completely clear on this one...
    CURSOR_HORIZONTAL_ABSOLUTE.execute(n)

def set_position(x=0, y=0):
    """Moves cursor to position row=x and col=y (x, y).
    NOTE: This assumes starting at (0, 0) which is different than the ANSI
    standard; it also assumes (x, y) and not (y, x) per ANSI standard."""
    CURSOR_SET_POSITION.execute(x, y)

def save_position():
    """Save the current cursor position."""
    CURSOR_SAVE_POSITION.execute()

def restore_position():
    """Restore the last saved cursor position."""
    CURSOR_RESTORE_POSITION.execute()

def get_position():
    """Returns a tuple of (x, y) of current cursor position.
    NOTE: this follows conventional (x, y) order and starts with (0, 0) and not
    the order according to the ANSI standard."""
    QCU = CSI + '6n'  # Query cursor position (to stdin)
    RCU = CSI + '{0};{1}R' # Reports Cursor positon (result from above query
                        # Reports as <ESC>[{row};{column}R
                        # Note that this is backwards order
    return (0, 0)

def row():
    """Returns the cursor's current row."""
    return x()

def col():
    """Returns the cursor's current column."""
    return y()

def x():
    """Returns the cursor's current row."""
    x, y = get_position()
    return x

def y(self):
    """Returns the cursor's current column."""
    x, y = get_position()
    return y
