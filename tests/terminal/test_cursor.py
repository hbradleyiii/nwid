#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_cursor.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       06/01/2017
#

"""
Unittests for nwid.terminal.cursor module.
"""

from __future__ import absolute_import

from mock import patch
from nwid.terminal import cursor
from nwid.terminal.codes import *
import pytest


## Cursor code escape sequence tests ##

@patch('sys.stdout.write')
def test_cursor_hide(mock_write):
    """Tests cusor.hide() escape sequence."""
    cursor.hide()
    mock_write.assert_called_once_with(CURSOR_HIDE.value)

@patch('sys.stdout.write')
def test_cursor_show(mock_write):
    """Tests cusor.show() escape sequence."""
    cursor.show()
    mock_write.assert_called_once_with(CURSOR_SHOW.value)

@patch('sys.stdout.write')
def test_cursor_move_up(mock_write):
    """Tests cusor.move_up() escape sequence."""
    cursor.move_up()
    mock_write.assert_called_once_with(CURSOR_UP.using(1))

@patch('sys.stdout.write')
def test_cursor_move_down(mock_write):
    """Tests cusor.move_down() escape sequence."""
    cursor.move_down()
    mock_write.assert_called_once_with(CURSOR_DOWN.using(1))

@patch('sys.stdout.write')
def test_cursor_move_left(mock_write):
    """Tests cusor.move_left() escape sequence."""
    cursor.move_left()
    mock_write.assert_called_once_with(CURSOR_LEFT.using(1))

@patch('sys.stdout.write')
def test_cursor_move_right(mock_write):
    """Tests cusor.move_right() escape sequence."""
    cursor.move_right()
    mock_write.assert_called_once_with(CURSOR_RIGHT.using(1))

@patch('sys.stdout.write')
def test_cursor_next_line(mock_write):
    """Tests cusor.next_line() escape sequence."""
    cursor.next_line()
    mock_write.assert_called_once_with(CURSOR_NEXT_LINE.using(1))

@patch('sys.stdout.write')
def test_cursor_previous_line(mock_write):
    """Tests cusor.previous_line() escape sequence."""
    cursor.previous_line()
    mock_write.assert_called_once_with(CURSOR_PREVIOUS_LINE.using(1))

@patch('sys.stdout.write')
def test_cursor_horizontal_absolute(mock_write):
    """Tests cusor.horizontal_absolute() escape sequence."""
    cursor.horizontal_absolute()
    mock_write.assert_called_once_with(CURSOR_HORIZONTAL_ABSOLUTE.using(1))

@patch('sys.stdout.write')
def test_cursor_set_position(mock_write):
    """Tests cusor.set_position() escape sequence."""
    cursor.set_position()
    mock_write.assert_called_once_with(CURSOR_SET_POSITION.using(0, 0))

@patch('sys.stdout.write')
def test_cursor_save_position(mock_write):
    """Tests cusor.save_position() escape sequence."""
    cursor.save_position()
    mock_write.assert_called_once_with(CURSOR_SAVE_POSITION.value)

@patch('sys.stdout.write')
def test_cursor_restore_position(mock_write):
    """Tests cusor.restore_position() escape sequence."""
    cursor.restore_position()
    mock_write.assert_called_once_with(CURSOR_RESTORE_POSITION.value)

@patch('sys.stdout.write')
def test_cursor_get_position(mock_write):
    """Tests cusor.get_position() escape sequence."""
    # TODO: Finish this
    # also: row, col, x, y
    pass
    cursor.get_position()
