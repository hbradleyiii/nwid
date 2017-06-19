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

from . import codes as code


def hide():
    """Hides the cursor."""
    code.CURSOR_HIDE()

def show():
    """Shows the cursor."""
    code.CURSOR_SHOW()

def move_up(n=1):
    """Moves your cursor up 'n' rows."""
    # TODO: is math correct here ?
    code.CURSOR_UP(n)

def move_down(n=1):
    """Moves your cursor down 'n' rows."""
    code.CURSOR_DOWN(n)

def move_left(n=1):
    """Moves your cursor left (backward) 'n' characters."""
    code.CURSOR_LEFT(n)

def move_right(n=1):
    """Moves your cursor right (forward) 'n' characters."""
    code.CURSOR_RIGHT(n)

def next_line(n=1):
    """Moves your cursor (up) to the start of the next 'n'th line."""
    code.CURSOR_NEXT_LINE(n)

def previous_line(n=1):
    """Moves your cursor (down) to the start of the previous 'n'th line."""
    code.CURSOR_PREVIOUS_LINE(n)

def horizontal_absolute(n=1):
    """Moves your cursor to the 'n' column."""
    # TODO: not completely clear on this one...
    code.CURSOR_HORIZONTAL_ABSOLUTE(n)

def set_position(row=0, col=0):
    """Moves cursor to position (row, col)."""
    code.CURSOR_SET_POSITION(row, col)

def save_position():
    """Save the current cursor position."""
    code.CURSOR_SAVE_POSITION()

def restore_position():
    """Restore the last saved cursor position."""
    code.CURSOR_RESTORE_POSITION()

def get_position():
    """Returns a tuple of (row, col) of current cursor position."""
    code.QCU = code.CSI + '6n'  # Query cursor position (to stdin)
    code.RCU = code.CSI + '{0};{1}R' # Reports Cursor positon (result from above query
                        # Reports as <ESC>[{row};{column}R
                        # Note that this is backwards order
    return (0, 0)

def row():
    """Returns the cursor's current row."""
    row, col = get_position()
    return row()

def col():
    """Returns the cursor's current column."""
    row, col = get_position()
    return col()
