#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_screen.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       06/01/2017
#

"""
Unittests for nwid.terminal.screen module.

Note: screen.size() is not tested here.
"""

from __future__ import absolute_import

from mock import patch
from nwid.terminal import screen
from nwid.terminal.codes import *
import pytest


## Screen code escape sequence tests ##

@patch('sys.stdout.write')
def test_screen_clear(mock_write):
    """Tests screen.clear() escape sequence."""
    screen.clear()
    mock_write.assert_called_once_with(CLEAR_SCREEN.value)

@patch('sys.stdout.write')
def test_screen_clear_down(mock_write):
    """Tests screen.clear_down() escape sequence."""
    screen.clear_down()
    mock_write.assert_called_once_with(CLEAR_DOWN.value)

@patch('sys.stdout.write')
def test_screen_clear_up(mock_write):
    """Tests screen.clear_up() escape sequence."""
    screen.clear_up()
    mock_write.assert_called_once_with(CLEAR_UP.value)

@patch('sys.stdout.write')
def test_screen_clear_line(mock_write):
    """Tests screen.clear_line() escape sequence."""
    screen.clear_line()
    mock_write.assert_called_once_with(CLEAR_LINE.value)

@patch('sys.stdout.write')
def test_screen_clear_line_forward(mock_write):
    """Tests screen.clear_line_forward() escape sequence."""
    screen.clear_line_forward()
    mock_write.assert_called_once_with(CLEAR_LINE_FORWARD.value)

@patch('sys.stdout.write')
def test_screen_clear_line_backward(mock_write):
    """Tests screen.clear_line_backward() escape sequence."""
    screen.clear_line_backward()
    mock_write.assert_called_once_with(CLEAR_LINE_BACKWARD.value)

@patch('sys.stdout.write')
def test_screen_reset(mock_write):
    """Tests screen.reset() escape sequence."""
    screen.reset()
    mock_write.assert_any_call(CURSOR_SET_POSITION.using(0,0))
    mock_write.assert_any_call(CLEAR_SCREEN.value)
