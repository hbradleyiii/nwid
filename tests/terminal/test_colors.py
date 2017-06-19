#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_colors.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       06/17/2017
#

"""
Unittests for nwid.terminal.colors module.
"""

from __future__ import absolute_import

from nwid.terminal import codes as code
from nwid.terminal import colors as color
from nwid.terminal import sgr


## Terminal color function tests ##

def tests_color_functions_wrap_text_with_escape_code():
    """A color function should wrap its text with the appropriate escape
    code."""
    string = 'This is sample text.'
    desired_string = sgr.create(code.RED) + 'This is sample text.' + sgr.reset()
    assert color.red(string) == desired_string

    desired_string = sgr.create(code.UNDERLINE) + 'This is sample text.' + sgr.reset()
    assert color.underline(string) == desired_string

    desired_string = sgr.create(code.BG_RED) + 'This is sample text.' + sgr.reset()
    assert color.bg_red(string) == desired_string

def tests_color_functions_can_wrap_text_with_existing_escape_code():
    """A color function can wrap test that already has existing escape
    code(s)."""
    string = 'This is ' + sgr.create(code.UNDERLINE) + 'sample' + sgr.reset() \
            + ' text.'
    desired_string = sgr.create(code.RED) + 'This is ' + sgr.create(code.UNDERLINE) + 'sample' + sgr.reset() \
            + sgr.create(code.RED) + ' text.' + sgr.reset()
    assert color.red(string) == desired_string

    desired_string = sgr.create(code.BG_RED) + 'This is ' + sgr.create(code.UNDERLINE) + 'sample' + sgr.reset() \
            + sgr.create(code.BG_RED) + ' text.' + sgr.reset()
    assert color.on_red(string) == desired_string

    desired_string = sgr.create(code.BOLD) + 'This is ' + sgr.create(code.UNDERLINE) + 'sample' + sgr.reset() \
            + sgr.create(code.BOLD) + ' text.' + sgr.reset()
    assert color.bold(string) == desired_string

def tests_color_on_color_functions_wrap_text_with_multiple_escape_codes():
    """A color function should wrap its text with the appropriate escape
    code."""
    string = 'This is sample text.'
    desired_string = sgr.create(code.BG_WHITE, code.RED) + 'This is sample text.' + sgr.reset()
    assert color.red_on_white(string) == desired_string

    desired_string = sgr.create(code.BG_BLUE, code.WHITE) + 'This is sample text.' + sgr.reset()
    assert color.white_on_blue(string) == desired_string

def tests_color_functions_can_be_nested():
    """Multiple color functions can be nested for recursion.
    The order of appliation is the order in which they appear."""
    string = 'This is sample text.'
    desired_string = sgr.create(code.BG_WHITE) + sgr.create(code.RED) + 'This is sample text.' + sgr.reset()
    assert color.bg_white(color.red(string)) == desired_string

def tests_color_functions_can_be_passed_as_attribute_arguments():
    """A color function can take other color functions as arguments to
    apply."""
    string = 'This is sample text.'
    desired_string = sgr.create(code.BG_WHITE, code.RED) + 'This is sample text.' + sgr.reset()
    assert color.bg_white(string, color.red) == desired_string

    desired_string = sgr.create(code.GREEN, code.BG_WHITE, code.UNDERLINE) + 'This is sample text.' + sgr.reset()
    assert color.green(string, color.on_white, color.underline) == desired_string

def tests_color_functions_can_be_chained_together_and_nested():
    """A color function can be nested and can take other color functions as
    arguments at the same time."""
    test_string = color.bg_white(
        'magenta on white ' +
        color.green('green (on white) ') +
        color.blue_on_yellow('blue on yellow ' + 
                             color.black_on_magenta('black on magenta ')) +
        color.red('red on black ' + color.green('green (on black) '),
                  color.on_black) +
        ' back to default (magenta on white)', color.magenta
    )

    desired_string = \
        sgr.create(code.BG_WHITE, code.MAGENTA) + 'magenta on white ' + \
        sgr.create(code.GREEN) + 'green (on white) ' + sgr.reset() + \
        sgr.create(code.BG_WHITE, code.MAGENTA) + \
        sgr.create(code.BG_YELLOW, code.BLUE) + 'blue on yellow ' + \
        sgr.create(code.BG_MAGENTA, code.BLACK) + 'black on magenta ' + \
        sgr.reset() + \
        sgr.create(code.BG_WHITE, code.MAGENTA) + \
        sgr.create(code.RED, code.BG_BLACK) + 'red on black ' + \
        sgr.create(code.GREEN) + 'green (on black) ' + sgr.reset() + \
        sgr.create(code.BG_WHITE, code.MAGENTA) + \
        ' back to default (magenta on white)' + sgr.reset()

    assert test_string == desired_string 
