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

from nwid import terminal
from nwid.terminal.codes import *
import pytest


## Terminal Code initialization test ##

def test_code_initialization():
    assert str(terminal.BLACK) == '30'
    assert terminal.BLACK.value == '30'
    assert BLACK + ';' == '30;'
    assert BLACK.group == 'fg_color'


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

def test_TerminalCode_can_be_used_with_args():
    """A TerminalCode object can be concatenated with a string."""
    terminal_code_1 = TerminalCode('name-1', 'abc{}')
    terminal_code_2 = TerminalCode('name-2', 'abc{}123{}567{}')
    assert str(terminal_code_1.using('d')) == 'abcd'
    assert str(terminal_code_2.using('d', '4', '8')) == 'abcd12345678'

def test_TerminalCode_with_placeholder_but_no_args_defaults_to_1():
    """A TerminalCode object can be concatenated with a string."""
    terminal_code_1 = TerminalCode('name-1', 'abc{}')
    terminal_code_2 = TerminalCode('name-2', 'abc{}123{}567{}')
    assert str(terminal_code_1) == 'abc1'
    assert str(terminal_code_2) == 'abc112315671'
