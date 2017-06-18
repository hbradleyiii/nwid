#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             sgr.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       05/29/2017
#

"""
nwid.terminal.sgr
~~~~~~~~~~~~~~~~~

This module contains functions for creating SGR (Select Graphic Rendition)
escape sequences.
"""

from __future__ import absolute_import

from nwid.terminal import codes as code

## SGR Exceptions ##

class SGRFGColorError(Exception): pass
class SGRBGColorError(Exception): pass
class SGRError(Exception): pass


## SGR Create functions ##

def create(*args):
    """Returns an SGR (Select Graphic Rendition) escape sequence given one or
    more attributes."""
    if not args:
        return ''
    return code.CSI + _combine_sgr_codes(*args) + 'm'

def reset():
    """Returns the escape sequence to reset the terminal to default."""
    return create(code.RESET)

def wrap(string, *args):
    """Takes a string and wraps an ANSI SGR escape sequence around it.

    If a reset is found in the middle of the string, the attribute is set again
    immediately following the reset. The entire string is concluded with the
    reset. This allows for unlimited nesting. (Without this, the first reset
    would clear the sequence for the entire rest of the string.)

    Note: Returned string will always end in a reset.

    :param string: the string around which to wrap the ANSI SGR escape sequence.
    :param *args: one or more escape args with which to put in one escape
        sequence.
    """
    # Remove trailing reset
    if string[-4:] == reset():
        string = string[:-4]

    _string = ''
    for _segment in string.split(reset()):
        _string = _string + create(*args) + _segment + reset()
    return _string


## SGR Helper Functions  ##

def _combine_sgr_codes(*codes):
    """Returns multiple attributes concatenated and separated by DELIMITER."""
    # Error checking:
    for code in codes:
        # Must be in one of these groups:
        if code.group not in [ 'style', 'fg_color', 'bg_color']:
            raise SGRError('Not an SGR code.')

    return _combine_attributes(*codes)

def _combine_attributes(*attributes):
    """Returns multiple attributes concatenated and separated by DELIMITER."""
    return reduce(lambda a, b: str(a) + code.DELIMITER + str(b), attributes)
