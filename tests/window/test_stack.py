#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_stack.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/09/2016
#

"""
Unittests for nwid.window.stack module.
"""

from __future__ import absolute_import

from nwid.exceptions import ExitNwidApp
from nwid.window import WindowStack
import pytest


def test_WindowStack_must_be_initialized_with_parent_app():
    """A WindowStack must be initialized with a parent app."""
    mock_app = 'MockApp'
    window_stack = WindowStack(mock_app)

    assert window_stack._parent_app == mock_app

    with pytest.raises(Exception):
        WindowStack()

def test_WindowStack_initializes_an_empty_list():
    """A WindowStack initializes an empty list."""
    mock_app = 'MockApp'
    window_stack = WindowStack(mock_app)

    assert window_stack._window_list == []

def test_WindowStack_can_append_new_windows_on_the_stack():
    """A WindowStack can append new windows onto the stack."""
    mock_app = 'MockApp'
    window_stack = WindowStack(mock_app)

    window_stack.append('mock_window')
    assert window_stack._window_list == ['mock_window']

    window_stack.append('mock_window_2')
    assert window_stack._window_list == ['mock_window', 'mock_window_2']

def test_WindowStack_can_pop_an_old_windows_off_the_stack():
    """A WindowStack can pop an old window off the stack."""
    mock_app = 'MockApp'
    window_stack = WindowStack(mock_app)

    window_stack.append('mock_window')
    window_stack.append('mock_window_2')

    window_stack.pop()
    assert window_stack._window_list == ['mock_window']

    window_stack.pop()
    assert window_stack._window_list == []

def test_popping_from_a_WindowStack_returns_the_topmost_window():
    """When popping, a WindowStack returns the topmost window."""
    mock_app = 'MockApp'
    window_stack = WindowStack(mock_app)

    window_stack.append(1)
    window_stack.append(2)
    window_stack.append(3)

    assert window_stack.pop() == 3
    assert window_stack.pop() == 2
    assert window_stack.pop() == 1

def test_WindowStack_raises_ExitNwidApp_when_popping_an_empty_list():
    """When popping from a stack with no more windows, WindowStack raises
    ExitNwidApp."""
    mock_app = 'MockApp'
    window_stack = WindowStack(mock_app)

    with pytest.raises(ExitNwidApp):
        window_stack.pop()

def test_WindowStack_has_a_top_property():
    """A WindowStack's top property returns the topmost window."""
    mock_app = 'MockApp'
    window_stack = WindowStack(mock_app)

    window_stack.append(1)
    window_stack.append(2)
    window_stack.append(3)

    assert window_stack.top == 3
    window_stack.pop()

    assert window_stack.top == 2
    window_stack.pop()

    assert window_stack.top == 1

def test_WindowStack_raises_ExitNwidApp_when_accessing_top_with_no_windows():
    """When accessing top with an empty stack, WindowStack raises ExitNwidApp."""
    mock_app = 'MockApp'
    window_stack = WindowStack(mock_app)

    with pytest.raises(ExitNwidApp):
        window_stack.pop()

def test_WindowStack_can_be_iterated_over():
    """A WindowStack can be iterated over in a loop."""
    mock_app = 'MockApp'
    window_stack = WindowStack(mock_app)

    window_stack.append(1)  # Append a mock window
    window_stack.append(2)
    window_stack.append(3)
    window_stack.append(4)
    window_stack.append(5)

    n = 0
    for window in window_stack:
        n += 1
        assert window == n
    assert n == 5
