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

from nwid.terminal.codes import *
from nwid.terminal import sgr
import pytest


## SGR unit tests ##

def test_sgr_codes():
    assert sgr.create(BLACK) == CSI + BLACK + 'm'
    assert sgr.create(BG_BLACK) == CSI + BG_BLACK + 'm'

def test_can_combine_sgr_codes():
    assert sgr.create(BLACK, BG_RED) == CSI + BLACK + DELIMITER + BG_RED+ 'm'
    assert sgr.create(UNDERLINE, BLACK, BG_RED) == \
        CSI + UNDERLINE + DELIMITER + BLACK + DELIMITER + BG_RED+ 'm'

def test_cannot_combine_multiple_sgr_fg_colors():
    with pytest.raises(sgr.SGRFGColorError):
        sgr.create(BLACK, RED)

def test_cannot_combine_multiple_sgr_bg_colors():
    with pytest.raises(sgr.SGRBGColorError):
        sgr.create(BG_BLACK, BG_RED)

def test_cannot_use_non_sgr_escape_sequence_as_sgr():
    with pytest.raises(sgr.SGRError):
        sgr.create(CURSOR_HIDE)

def test_sgr_reset():
    assert sgr.create(RESET) == sgr.reset()
