#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             colors.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/23/2016
#

"""
nwid.terminal.colors
~~~~~~~~~~~~~~~~~~~~

Functions for creating and combining terminal text effects and colors using
code escape sequences.

They return the modified string with the appropriate escape sequences.
"""

from __future__ import absolute_import

from . import codes as code
from . import sgr


def _combine(string, attribute, *funcs, **additional):
    """Recursively Combines multiple sgr attributes into one string using
    sgr.wrap.

    This is called by individual attribute functions and allows either chaining
    multiple functions or passing attribute functions as arguments of other
    attribute functions.

    :param string: the string around which to wrap the SGR codes.
    :param attribute: the code attribute to be used and combined with optional
        additional attributes.
    :param *funcs: optional attribute functions to be applied.
    :param **additional: additional attributes to be combined with attribute.
        This parameter is intended for internal use for recursion.
        In **additional is additional['attributes'] which is a tuple of
        attributes to be ultimately combined with sgr_wrap.

    Usage::
        >>> print(bold('The important string.' red, on_white))
        The important string.
        >>> print(bold(red(on_white('The important string.'))))
        The important string.

    """
    _attributes = additional['attributes'] + (attribute,) \
        if 'attributes' in additional else (attribute,)
    if funcs:
        _additional = {'attributes' : _attributes}
        _next_func, _funcs = funcs[0], funcs[1:]
        return _next_func(string, *_funcs, **_additional)
    else:
        return sgr.wrap(string, *_attributes)


# Text effects

def normal(string, *funcs, **additional):
    """Text effect - normal. (see _combine())."""
    return _combine(string, code.RESET, *funcs, **additional)

def underline(string, *funcs, **additional):
    """Text effect - underline. (see _combine())."""
    return _combine(string, code.UNDERLINE, *funcs, **additional)

def bold(string, *funcs, **additional):
    """Text effect - bold. (see _combine())."""
    return _combine(string, code.BOLD, *funcs, **additional)

def blink(string, *funcs, **additional):
    """Text effect - blink. (see _combine())."""
    return _combine(string, code.BLINK, *funcs, **additional)

def rblink(string, *funcs, **additional):
    """Text effect - rblink. (see _combine())."""
    return _combine(string, code.RBLINK, *funcs, **additional)

def reverse(string, *funcs, **additional):
    """Text effect - reverse. (see _combine())."""
    return _combine(string, code.REVERSE, *funcs, **additional)

def conceal(string, *funcs, **additional):
    """Text effect - conceal. (see _combine())."""
    return _combine(string, code.CONCEAL, *funcs, **additional)


# Basic colors

def black(string, *funcs, **additional):
    """Text color - black. (see _combine())."""
    return _combine(string, code.BLACK, *funcs, **additional)

def red(string, *funcs, **additional):
    """Text color - red. (see _combine())."""
    return _combine(string, code.RED, *funcs, **additional)

def green(string, *funcs, **additional):
    """Text color - green. (see _combine())."""
    return _combine(string, code.GREEN, *funcs, **additional)

def yellow(string, *funcs, **additional):
    """Text color - yellow. (see _combine())."""
    return _combine(string, code.YELLOW, *funcs, **additional)

def blue(string, *funcs, **additional):
    """Text color - blue. (see _combine())."""
    return _combine(string, code.BLUE, *funcs, **additional)

def magenta(string, *funcs, **additional):
    """Text color - magenta. (see _combine())."""
    return _combine(string, code.MAGENTA, *funcs, **additional)

def cyan(string, *funcs, **additional):
    """Text color - cyan. (see _combine())."""
    return _combine(string, code.CYAN, *funcs, **additional)

def white(string, *funcs, **additional):
    """Text color - white. (see _combine())."""
    return _combine(string, code.WHITE, *funcs, **additional)


# Basic background colors

def bg_black(string, *funcs, **additional):
    """Text background color - black. (see _combine())."""
    return _combine(string, code.BG_BLACK, *funcs, **additional)

def bg_red(string, *funcs, **additional):
    """Text background color - red. (see _combine())."""
    return _combine(string, code.BG_RED, *funcs, **additional)

def bg_green(string, *funcs, **additional):
    """Text background color - green. (see _combine())."""
    return _combine(string, code.BG_GREEN, *funcs, **additional)

def bg_yellow(string, *funcs, **additional):
    """Text background color - yellow. (see _combine())."""
    return _combine(string, code.BG_YELLOW, *funcs, **additional)

def bg_blue(string, *funcs, **additional):
    """Text background color - blue. (see _combine())."""
    return _combine(string, code.BG_BLUE, *funcs, **additional)

def bg_magenta(string, *funcs, **additional):
    """Text background color - magenta. (see _combine())."""
    return _combine(string, code.BG_MAGENTA, *funcs, **additional)

def bg_cyan(string, *funcs, **additional):
    """Text background color - cyan. (see _combine())."""
    return _combine(string, code.BG_CYAN, *funcs, **additional)

def bg_white(string, *funcs, **additional):
    """Text background color - white. (see _combine())."""
    return _combine(string, code.BG_WHITE, *funcs, **additional)



def on_black(string, *funcs, **additional):
    """Text background color - black. (see _combine())."""
    return bg_black(string, *funcs, **additional)

def on_red(string, *funcs, **additional):
    """Text background color - red. (see _combine())."""
    return bg_red(string, *funcs, **additional)

def on_green(string, *funcs, **additional):
    """Text background color - green. (see _combine())."""
    return bg_green(string, *funcs, **additional)

def on_yellow(string, *funcs, **additional):
    """Text background color - yellow. (see _combine())."""
    return bg_yellow(string, *funcs, **additional)

def on_blue(string, *funcs, **additional):
    """Text background color - blue. (see _combine())."""
    return bg_blue(string, *funcs, **additional)

def on_magenta(string, *funcs, **additional):
    """Text background color - magenta. (see _combine())."""
    return bg_magenta(string, *funcs, **additional)

def on_cyan(string, *funcs, **additional):
    """Text background color - cyan. (see _combine())."""
    return bg_cyan(string, *funcs, **additional)

def on_white(string, *funcs, **additional):
    """Text background color - white. (see _combine())."""
    return bg_white(string, *funcs, **additional)


# Colors on a black background
def red_on_black(string, *funcs, **additional):
    """Text color - red on background color - black. (see _combine())."""
    return _combine(string, code.RED, *funcs, attributes=(code.BG_BLACK,))

def green_on_black(string, *funcs, **additional):
    """Text color - green on background color - black. (see _combine())."""
    return _combine(string, code.GREEN, *funcs, attributes=(code.BG_BLACK,))

def yellow_on_black(string, *funcs, **additional):
    """Text color - yellow on background color - black. (see _combine())."""
    return _combine(string, code.YELLOW, *funcs, attributes=(code.BG_BLACK,))

def blue_on_black(string, *funcs, **additional):
    """Text color - blue on background color - black. (see _combine())."""
    return _combine(string, code.BLUE, *funcs, attributes=(code.BG_BLACK,))

def magenta_on_black(string, *funcs, **additional):
    """Text color - magenta on background color - black. (see _combine())."""
    return _combine(string, code.MAGENTA, *funcs, attributes=(code.BG_BLACK,))

def cyan_on_black(string, *funcs, **additional):
    """Text color - cyan on background color - black. (see _combine())."""
    return _combine(string, code.CYAN, *funcs, attributes=(code.BG_BLACK,))

def white_on_black(string, *funcs, **additional):
    """Text color - white on background color - black. (see _combine())."""
    return _combine(string, code.WHITE, *funcs, attributes=(code.BG_BLACK,))


# Colors on a red background

def black_on_red(string, *funcs, **additional):
    """Text color - black on background color - red. (see _combine())."""
    return _combine(string, code.BLACK, *funcs, attributes=(code.BG_RED,))

def green_on_red(string, *funcs, **additional):
    """Text color - green on background color - red. (see _combine())."""
    return _combine(string, code.GREEN, *funcs, attributes=(code.BG_RED,))

def yellow_on_red(string, *funcs, **additional):
    """Text color - yellow on background color - red. (see _combine())."""
    return _combine(string, code.YELLOW, *funcs, attributes=(code.BG_RED,))

def blue_on_red(string, *funcs, **additional):
    """Text color - blue on background color - red. (see _combine())."""
    return _combine(string, code.BLUE, *funcs, attributes=(code.BG_RED,))

def magenta_on_red(string, *funcs, **additional):
    """Text color - magenta on background color - red. (see _combine())."""
    return _combine(string, code.MAGENTA, *funcs, attributes=(code.BG_RED,))

def cyan_on_red(string, *funcs, **additional):
    """Text color - cyan on background color - red. (see _combine())."""
    return _combine(string, code.CYAN, *funcs, attributes=(code.BG_RED,))

def white_on_red(string, *funcs, **additional):
    """Text color - white on background color - red. (see _combine())."""
    return _combine(string, code.WHITE, *funcs, attributes=(code.BG_RED,))


# Colors on a green background

def black_on_green(string, *funcs, **additional):
    """Text color - black on background color - green. (see _combine())."""
    return _combine(string, code.BLACK, *funcs, attributes=(code.BG_GREEN,))

def red_on_green(string, *funcs, **additional):
    """Text color - red on background color - green. (see _combine())."""
    return _combine(string, code.RED, *funcs, attributes=(code.BG_GREEN,))

def yellow_on_green(string, *funcs, **additional):
    """Text color - yellow on background color - green. (see _combine())."""
    return _combine(string, code.YELLOW, *funcs, attributes=(code.BG_GREEN,))

def blue_on_green(string, *funcs, **additional):
    """Text color - blue on background color - green. (see _combine())."""
    return _combine(string, code.BLUE, *funcs, attributes=(code.BG_GREEN,))

def magenta_on_green(string, *funcs, **additional):
    """Text color - magenta on background color - green. (see _combine())."""
    return _combine(string, code.MAGENTA, *funcs, attributes=(code.BG_GREEN,))

def cyan_on_green(string, *funcs, **additional):
    """Text color - cyan on background color - green. (see _combine())."""
    return _combine(string, code.CYAN, *funcs, attributes=(code.BG_GREEN,))

def white_on_green(string, *funcs, **additional):
    """Text color - white on background color - green. (see _combine())."""
    return _combine(string, code.WHITE, *funcs, attributes=(code.BG_GREEN,))


# Colors on a yellow background

def black_on_yellow(string, *func, **additional):
    """Text color - black on background color - yellow. (see _combine())."""
    return _combine(string, code.BLACK, *func, attributes=(code.BG_YELLOW,))

def red_on_yellow(string, *funcs, **additional):
    """Text color - red on background color - yellow. (see _combine())."""
    return _combine(string, code.RED, *funcs, attributes=(code.BG_YELLOW,))

def green_on_yellow(string, *funcs, **additional):
    """Text color - green on background color - yellow. (see _combine())."""
    return _combine(string, code.GREEN, *funcs, attributes=(code.BG_YELLOW,))

def blue_on_yellow(string, *funcs, **additional):
    """Text color - blue on background color - yellow. (see _combine())."""
    return _combine(string, code.BLUE, *funcs, attributes=(code.BG_YELLOW,))

def magenta_on_yellow(string, *funcs, **additional):
    """Text color - magenta on background color - yellow. (see _combine())."""
    return _combine(string, code.MAGENTA, *funcs, attributes=(code.BG_YELLOW,))

def cyan_on_yellow(string, *funcs, **additional):
    """Text color - cyan on background color - yellow. (see _combine())."""
    return _combine(string, code.CYAN, *funcs, attributes=(code.BG_YELLOW,))

def white_on_yellow(string, *funcs, **additional):
    """Text color - white on background color - yellow. (see _combine())."""
    return _combine(string, code.WHITE, *funcs, attributes=(code.BG_YELLOW,))


# Colors on a blue background

def black_on_blue(string, *funcs, **additional):
    """Text color - black on background color - blue. (see _combine())."""
    return _combine(string, code.BLACK, *funcs, attributes=(code.BG_BLUE,))

def red_on_blue(string, *funcs, **additional):
    """Text color - red on background color - blue. (see _combine())."""
    return _combine(string, code.RED, *funcs, attributes=(code.BG_BLUE,))

def green_on_blue(string, *funcs, **additional):
    """Text color - green on background color - blue. (see _combine())."""
    return _combine(string, code.GREEN, *funcs, attributes=(code.BG_BLUE,))

def yellow_on_blue(string, *funcs, **additional):
    """Text color - yellow on background color - blue. (see _combine())."""
    return _combine(string, code.YELLOW, *funcs, attributes=(code.BG_BLUE,))

def magenta_on_blue(string, *funcs, **additional):
    """Text color - magenta on background color - blue. (see _combine())."""
    return _combine(string, code.MAGENTA, *funcs, attributes=(code.BG_BLUE,))

def cyan_on_blue(string, *funcs, **additional):
    """Text color - cyan on background color - blue. (see _combine())."""
    return _combine(string, code.CYAN, *funcs, attributes=(code.BG_BLUE,))

def white_on_blue(string, *funcs, **additional):
    """Text color - white on background color - blue. (see _combine())."""
    return _combine(string, code.WHITE, *funcs, attributes=(code.BG_BLUE,))


# Colors on a magenta background

def black_on_magenta(string, *funcs, **additional):
    """Text color - black on background color - magenta. (see _combine())."""
    return _combine(string, code.BLACK, *funcs, attributes=(code.BG_MAGENTA,))

def red_on_magenta(string, *funcs, **additional):
    """Text color - red on background color - magenta. (see _combine())."""
    return _combine(string, code.RED, *funcs, attributes=(code.BG_MAGENTA,))

def green_on_magenta(string, *funcs, **additional):
    """Text color - green on background color - magenta. (see _combine())."""
    return _combine(string, code.GREEN, *funcs, attributes=(code.BG_MAGENTA,))

def yellow_on_magenta(string, *funcs, **additional):
    """Text color - yellow on background color - magenta. (see _combine())."""
    return _combine(string, code.YELLOW, *funcs, attributes=(code.BG_MAGENTA,))

def blue_on_magenta(string, *funcs, **additional):
    """Text color - blue on background color - magenta. (see _combine())."""
    return _combine(string, code.BLUE, *funcs, attributes=(code.BG_MAGENTA,))

def cyan_on_magenta(string, *funcs, **additional):
    """Text color - cyan on background color - magenta. (see _combine())."""
    return _combine(string, code.CYAN, *funcs, attributes=(code.BG_MAGENTA,))

def white_on_magenta(string, *funcs, **additional):
    """Text color - white on background color - magenta. (see _combine())."""
    return _combine(string, code.WHITE, *funcs, attributes=(code.BG_MAGENTA,))


# Colors on a cyan background

def black_on_cyan(string, *funcs, **additional):
    """Text color - black on background color - cyan. (see _combine())."""
    return _combine(string, code.BLACK, *funcs, attributes=(code.BG_CYAN,))

def red_on_cyan(string, *funcs, **additional):
    """Text color - red on background color - cyan. (see _combine())."""
    return _combine(string, code.RED, *funcs, attributes=(code.BG_CYAN,))

def green_on_cyan(string, *funcs, **additional):
    """Text color - green on background color - cyan. (see _combine())."""
    return _combine(string, code.GREEN, *funcs, attributes=(code.BG_CYAN,))

def yellow_on_cyan(string, *funcs, **additional):
    """Text color - yellow on background color - cyan. (see _combine())."""
    return _combine(string, code.YELLOW, *funcs, attributes=(code.BG_CYAN,))

def blue_on_cyan(string, *funcs, **additional):
    """Text color - blue on background color - cyan. (see _combine())."""
    return _combine(string, code.BLUE, *funcs, attributes=(code.BG_CYAN,))

def magenta_on_cyan(string, *funcs, **additional):
    """Text color - magenta on background color - cyan. (see _combine())."""
    return _combine(string, code.MAGENTA, *funcs, attributes=(code.BG_CYAN,))

def white_on_cyan(string, *funcs, **additional):
    """Text color - white on background color - cyan. (see _combine())."""
    return _combine(string, code.WHITE, *funcs, attributes=(code.BG_CYAN,))


# Colors on a white background

def black_on_white(string, *funcs, **additional):
    """Text color - black on background color - white. (see _combine())."""
    return _combine(string, code.BLACK, *funcs, attributes=(code.BG_WHITE,))

def red_on_white(string, *funcs, **additional):
    """Text color - red on background color - white. (see _combine())."""
    return _combine(string, code.RED, *funcs, attributes=(code.BG_WHITE,))

def green_on_white(string, *funcs, **additional):
    """Text color - green on background color - white. (see _combine())."""
    return _combine(string, code.GREEN, *funcs, attributes=(code.BG_WHITE,))

def yellow_on_white(string, *funcs, **additional):
    """Text color - yellow on background color - white. (see _combine())."""
    return _combine(string, code.YELLOW, *funcs, attributes=(code.BG_WHITE,))

def blue_on_white(string, *funcs, **additional):
    """Text color - blue on background color - white. (see _combine())."""
    return _combine(string, code.BLUE, *funcs, attributes=(code.BG_WHITE,))

def magenta_on_white(string, *funcs, **additional):
    """Text color - magenta on background color - white. (see _combine())."""
    return _combine(string, code.MAGENTA, *funcs, attributes=(code.BG_WHITE,))

def cyan_on_white(string, *funcs, **additional):
    """Text color - cyan on background color - white. (see _combine())."""
    return _combine(string, code.CYAN, *funcs, attributes=(code.BG_WHITE,))
