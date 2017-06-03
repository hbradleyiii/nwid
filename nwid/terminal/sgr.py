#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             codes.py
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

from nwid.terminal.codes import *

## SGR Exceptions ##

class SGR_FGColorError(Exception): pass
class SGR_BGColorError(Exception): pass
class SGR_Error(Exception): pass


## SGR Create functions ##

def create(*args):
    """Returns an SGR (Select Graphic Rendition) escape sequence given one or
    more attributes."""
    if not args:
        return ''
    return CSI + _combine_sgr_codes(*args) + 'm'

def wrap(string, *args):
    """Returns the result of wrapping a string with the escape sequence."""
    return create(*args) + string + reset()

def reset():
    """Returns the escape sequence to reset the terminal to default."""
    return create(RESET)


## SGR Helper Functions  ##

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

    return _combine_attributes(*codes)

def _combine_attributes(*attributes):
    """Returns multiple attributes concatenated and separated by DELIMITER."""
    return reduce(lambda a, b: str(a) + DELIMITER + str(b), attributes)
