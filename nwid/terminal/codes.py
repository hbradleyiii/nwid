#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             codes.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       05/29/2017
#

"""
nwid.terminal.codes
~~~~~~~~~~~~~~~~~~~

This module contains common ANSI terminal codes used by nwid.

The codes are created at runtime each as a TerminalCode object. Doing it this
way gives the option to potentially adjust codes based on the machine or
pseudoterminal.
"""

from __future__ import absolute_import

from sys import modules, stdout


# Terminal code object #

class TerminalCode(object):
    """A terminal code object containing its name, value, and group"""

    def __init__(self, name, value, group=None):
        """Initializes a TerminalCode with a name, value, and optional
        group."""
        self.name = name
        self.value = value
        self.group = group

    def __str__(self):
        """Returns the string representation of the TerminalCode, replacing any
        placeholder with '1'."""
        if '{}' in self.value:
            return self.using(*('1',) * self.value.count('{}'))
        return str(self.value)

    def __repr__(self):
        return 'TODO:'

    def __add__(self, other):
        """Allow string concatenation."""
        return self.value + str(other)

    def __radd__(self, other):
        """Allow string concatenation."""
        return str(other) + self.value

    def __call__(self, *args):
        """Outputs (executes) an escape sequence."""
        stdout.write(self.using(*args))
        stdout.flush()

    def using(self, *args):
        """Replaces any placeholders ('{}') with *args."""
        return self.value.format(*args)


# Terminal codes initialization #

# General ASCII Codes

NULL =    '\00'   # Null character
BEL  =    '\007'  # Terminal Bell
BS   =    '\010'  # Backspace
HT   =    '\011'  # Horizontal Tab
LF   =    '\012'  # Linefeed (newline)
VT   =    '\013'  # Vertical Tab
FF   =    '\014'  # Formfeed (or NP: new page)
CR   =    '\015'  # Carriage Return
DEL  =    '\177'  # Delete character
ESC  =    '\033'  # Escape character
CSI  =    '\033[' # Used to initialize control sequences
OSI  =    '\033]'

DELIMITER = ';'

_codes = {

    # Cursor manipulation escape sequences

    'cursor_manipulation' : {
        'CURSOR_HIDE':                CSI + '?25l',
        'CURSOR_SHOW':                CSI + '?25h',
        'CURSOR_UP':                  CSI + '{}A',   # NOTE: {} must be replaced with an integer.
        'CURSOR_DOWN':                CSI + '{}B',
        'CURSOR_RIGHT':               CSI + '{}C',
        'CURSOR_LEFT':                CSI + '{}D',
        'CURSOR_NEXT_LINE':           CSI + '{}E',
        'CURSOR_PREVIOUS_LINE':       CSI + '{}F',
        'CURSOR_HORIZONTAL_ABSOLUTE': CSI + '{}G',
        'CURSOR_SET_POSITION':        CSI + '{};{}f',
        'CURSOR_GET_POSITION':        'TODO', # TODO
        'CURSOR_SAVE_POSITION':       CSI + 's',
        'CURSOR_RESTORE_POSITION':    CSI + 'u',
    },


    # Screen manipulation escape sequences

    'screen_manipulation' : {
        'CLEAR_SCREEN':        CSI + '2J',
        'CLEAR_DOWN':          CSI + '0J',
        'CLEAR_UP':            CSI + '1J',
        'CLEAR_LINE':          CSI + '2K',
        'CLEAR_LINE_FORWARD':  CSI + '0K',
        'CLEAR_LINE_BACKWARD': CSI + '1K',
    },


    # Terminal settings

    'terminal_settings': {
        'RESET_TERMINAL':    ESC + 'c',
        'ENABLE_LINE_WRAP':  CSI + '7h',
        'DISABLE_LINE_WRAP': CSI + '7l',
        'SET_SCROLL_ALL':    CSI + 'r',
        'SET_SCROLL':        CSI + '0;0r',
        'SCROLL_UP':         ESC + 'D',
        'SCROLL_DOWN':       ESC + 'M',
    },


    # SGR escape sequences (Colors/Styles)

    'style': {
        'RESET':        '0',
        'BOLD':         '1',
        'UNDERLINE':    '4',
        'BLINK':        '5',
        'RBLINK':       '6',
        'REVERSE':      '7',
        'CONCEAL':      '8',
    },

    'fg_color': {
        'BLACK':        '30',
        'RED':          '31',
        'GREEN':        '32',
        'YELLOW':       '33',
        'BLUE':         '34',
        'MAGENTA':      '35',
        'CYAN':         '36',
        'WHITE':        '37',
        'EXTENDED':     '38',
    },

    'bg_color': {
        'BG_BLACK':     '40',
        'BG_RED':       '41',
        'BG_GREEN':     '42',
        'BG_YELLOW':    '43',
        'BG_BLUE':      '44',
        'BG_MAGENTA':   '45',
        'BG_CYAN':      '46',
        'BG_WHITE':     '47',
        'BG_EXTENDED':  '48',
    }
}


# Initialize the TerminalCode object and make it available in this
# (nwid.terminal.codes) namespace:
for _group, _codes in _codes.items():
    for _name, _value in _codes.items():
        setattr(modules[__name__], _name, TerminalCode(_name, _value, _group))
