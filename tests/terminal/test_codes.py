#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_codes.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       05/29/2017
#

"""
Unittests for nwid.terminal.codes module.
"""

from __future__ import absolute_import

from nwid.terminal.codes import *
import pytest
import terminal


## Terminal Code functional tests ##

def test_code_initialization():
    assert terminal.code['BLACK'].name == 'BLACK'
    assert terminal.BLACK == terminal.code['BLACK'].value
    assert terminal.BLACK == str(terminal.code['BLACK'])
    assert terminal.BLACK + ';' == terminal.code['BLACK'] + ';'


## SGR functional tests ##

def test_sgr_codes():
    assert sgr(code['BLACK']) == terminal.CSI + terminal.BLACK + 'm'
    assert sgr(code['BG_BLACK']) == terminal.CSI + terminal.BG_BLACK + 'm'

def test_can_combine_sgr_codes():
    assert sgr(code['BLACK'], code['BG_RED']) == terminal.CSI + terminal.BLACK \
        + terminal.DELIMITER + terminal.BG_RED+ 'm'
    assert sgr(code['UNDERLINE'], code['BLACK'], code['BG_RED']) == \
        terminal.CSI + terminal.UNDERLINE + terminal.DELIMITER + \
        terminal.BLACK + terminal.DELIMITER + terminal.BG_RED+ 'm'

def test_cannot_combine_multiple_sgr_fg_colors():
    with pytest.raises(SGR_FGColorError):
        sgr(code['BLACK'], code['RED'])

def test_cannot_combine_multiple_sgr_bg_colors():
    print code['BLACK'].group
    with pytest.raises(SGR_BGColorError):
        sgr(code['BG_BLACK'], code['BG_RED'])

def test_sgr_reset():
    assert sgr(code['RESET']) == sgr_reset()


## Test TerminalCode object ##

def test_TerminalCode_has_a_name():
    """A TerminalCode object should have a name attribute."""
    terminal_code = TerminalCode('a-name', 'value')
    assert terminal_code.name == 'a-name'

def test_TerminalCode_has_a_value():
    """A TerminalCode object should have a value attribute."""
    terminal_code = TerminalCode('_', '123')
    assert terminal_code.value == '123'

def test_TerminalCode_string_is_its_value():
    """A TerminalCode object should have a value attribute."""
    terminal_code = TerminalCode('_', '123')
    assert str(terminal_code) == '123'
    assert terminal_code.__str__() == '123'

def test_TerminalCode_can_have_a_group():
    """A TerminalCode object can have a group attribute."""
    terminal_code = TerminalCode('_', '_', 'group')
    assert terminal_code.group == 'group'

def test_TerminalCode_can_be_concatenated_with_another():
    """A TerminalCode object can be concatenated with another."""
    terminal_code_1 = TerminalCode('name-1', 'value-1')
    terminal_code_2 = TerminalCode('name-2', 'value-2')
    assert terminal_code_1 + terminal_code_2 == 'value-1value-2'

def test_TerminalCode_can_be_concatenated_with_a_string():
    """A TerminalCode object can be concatenated with a string."""
    terminal_code = TerminalCode('name-1', 'value-1')
    string = 'value-2'
    assert terminal_code + string == 'value-1value-2'
