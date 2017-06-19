#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_sgr.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       06/01/2017
#

"""
Unittests for nwid.terminal.sgr module.
"""

from __future__ import absolute_import

from nwid.terminal import codes as code
from nwid.terminal import sgr
import pytest


## SGR unit tests ##

def test_sgr_can_create_codes():
    """SGR escape sequences can be combined to create one SGR code."""
    assert sgr.create(code.BLACK) == code.CSI + code.BLACK + 'm'
    assert sgr.create(code.BG_BLACK) == code.CSI + code.BG_BLACK + 'm'

def test_sgr_create():
    """SGR create returns an empty string when no args are passed."""
    assert sgr.create() == ''

def test_can_combine_sgr_codes():
    """Multiple SGR escape codes can be combined in one SGR code."""
    assert sgr.create(code.BLACK, code.BG_RED) == \
        code.CSI + code.BLACK + code.DELIMITER + code.BG_RED + 'm'
    assert sgr.create(code.UNDERLINE, code.BLACK, code.BG_RED) == \
        code.CSI + code.UNDERLINE + code.DELIMITER + code.BLACK + \
        code.DELIMITER + code.BG_RED + 'm'

def test_cannot_use_non_sgr_escape_sequence_as_sgr():
    """Only SGR escape sequences can be used as an SGR code."""
    with pytest.raises(sgr.SGRError):
        sgr.create(code.CURSOR_HIDE)

def test_sgr_reset():
    """SGR reset test."""
    assert sgr.create(code.RESET) == sgr.reset()
    assert sgr.reset() == code.CSI + code.RESET + 'm'

def test_can_wrap_string_with_sgr():
    """SGR function wrap can wrap a string with an SGR sequence ending in a
    reset."""
    assert sgr.wrap('This is a string.', code.BLACK, code.BG_RED) == \
        code.CSI + code.BLACK + code.DELIMITER + code.BG_RED + 'm' + \
        'This is a string.' + code.CSI + code.RESET + 'm'

def test_can_wrap_string_with_reset_with_sgr():
    """SGR function wrap can wrap a string with an SGR sequence ending in a
    reset."""
    string = 'This ' + sgr.create(code.RED) + 'is' + sgr.reset() + ' a string.'
    modified_string = sgr.create(code.BG_BLUE) + 'This ' + \
            sgr.create(code.RED) + 'is' + sgr.reset() + \
            sgr.create(code.BG_BLUE) + ' a string.' + sgr.reset()

    assert sgr.wrap(string, code.BG_BLUE) == modified_string

def test_can_wrap_string_with_trailing_reset_with_sgr():
    """SGR function wrap can wrap a string with an SGR sequence ending in a
    reset at the end of the string. The reset is not duplicated."""
    string = 'This ' + sgr.create(code.RED) + 'is a string.' + sgr.reset()
    modified_string = sgr.create(code.BG_BLUE) + 'This ' + \
            sgr.create(code.RED) + 'is a string.' + sgr.reset()

    assert sgr.wrap(string, code.BG_BLUE) == modified_string
