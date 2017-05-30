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

This module contains common ASCII/ANSI terminal codes and helper functions.
"""

from __future__ import absolute_import

import sys


# SGR Exceptions

class SGR_FGColorError(Exception): pass
class SGR_BGColorError(Exception): pass
class SGR_Error(Exception): pass


# Functions for creating SGR escape sequences

def _combine_sgr_codes(*codes):
    """Returns multiple attributes concatenated and separated by DELIMITER."""
    has_fg_code = False
    has_bg_code = False

    # Error checking:
    for code in codes:
        # Must be in one of these groups:
        if code.group not in [ 'style', 'fg_color', 'bg_color']:
            raise SGR_Error('Not an SGR code.')

        # Should only have one foreground color:
        if code.group == 'fg_color':
            if has_fg_code:
                raise SGR_FGColorError('Cannot have multiple foreground colors\
                                       at the same time.')
            else:
                has_fg_code = True

        # Should only have one background color:
        if code.group == 'bg_color':
            if has_bg_code:
                raise SGR_BGColorError('Cannot have multiple background colors\
                                       at the same time.')
            else:
                has_bg_code = True

    return reduce(lambda a, b: str(a) + DELIMITER + str(b), codes)

def sgr(*args):
    """Returns an SGR (Select Graphic Rendition) escape sequence given one or
    more attributes."""
    if not args:
        return ''
    return CSI + _combine_sgr_codes(*args) + 'm'

def sgr_reset():
    """Returns the escape sequence to reset the terminal to default."""
    return sgr(code['RESET'])


# Terminal code object & terminal codes initialization

class TerminalCode(object):
    """A terminal code object containing its name, value, and group"""
    def __init__(self, name, value, group=None):
        self.name = name
        self.value = value
        self.group = group

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return 'TODO:'

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return other + self.value


_codes = {

    # General ASCII Codes

    'ascii_general' : {
        'NULL':   '\00',   # Null character
        'BEL':    '\007',  # Terminal Bell
        'BS':     '\010',  # Backspace
        'HT':     '\011',  # Horizontal Tab
        'LF':     '\012',  # Linefeed (newline)
        'VT':     '\013',  # Vertical Tab
        'FF':     '\014',  # Formfeed (or NP: new page)
        'CR':     '\015',  # Carriage Return
        'ESC':    '\033',  # Escape character
        'DEL':    '\177',  # Delete character
    },


    # Escape Sequences

    'meta_sequences' : {
        'CSI':       '\033[',
        'OSC':       '\033]',
        'DELIMITER': ';',
    },


    # Colors/Styles

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

code = dict()

for group, codes in _codes.items():
    for _code, value in codes.items():
        # Create the dict:
        code[_code] = TerminalCode(_code, value, group)

        # Also, Make the variable available in this (nwid.terminal) namespace:
        setattr(sys.modules[__name__], _code, value)
