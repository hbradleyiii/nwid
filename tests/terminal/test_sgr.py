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

def test_sgr_codes():
    """SGR escape sequences can be combined to create one SGR code."""
    assert sgr.create(code.BLACK) == code.CSI + code.BLACK + 'm'
    assert sgr.create(code.BG_BLACK) == code.CSI + code.BG_BLACK + 'm'

def test_can_combine_sgr_codes():
    """Multiple SGR escape codes can be combined in one SGR code."""
    assert sgr.create(code.BLACK, code.BG_RED) == \
        code.CSI + code.BLACK + code.DELIMITER + code.BG_RED+ 'm'
    assert sgr.create(code.UNDERLINE, code.BLACK, code.BG_RED) == \
        code.CSI + code.UNDERLINE + code.DELIMITER + code.BLACK + \
        code.DELIMITER + code.BG_RED + 'm'

def test_cannot_combine_multiple_sgr_fg_colors():
    """Multiple foreground colors cannot be combined in one SGR code."""
    with pytest.raises(sgr.SGRFGColorError):
        sgr.create(code.BLACK, code.RED)

def test_cannot_combine_multiple_sgr_bg_colors():
    """Multiple background colors cannot be combined in one SGR code."""
    with pytest.raises(sgr.SGRBGColorError):
        sgr.create(code.BG_BLACK, code.BG_RED)

def test_cannot_use_non_sgr_escape_sequence_as_sgr():
    """Only SGR escape sequences can be used as an SGR code."""
    with pytest.raises(sgr.SGRError):
        sgr.create(code.CURSOR_HIDE)

def test_sgr_reset():
    """SGR reset test."""
    assert sgr.create(code.RESET) == sgr.reset()
