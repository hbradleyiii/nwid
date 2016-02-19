#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_events.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/19/2016
#

"""
Unittests for nwid.events module.
"""

import pytest
from nwid.events import HandlerList

def mock_callback():
    return True

def mock_wrong_callback():
    return False


## Test data structure HandlerList ##

def test_handlerlist_add():
    """Tests adding an item to a HandlerList."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1)
    assert handler_list._list[0] == handler_list.Item(mock_callback, 1)

def test_handlerlist_add_multiple():
    """Tests the list order from adding multiple items with different priorities out of order."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1)
    handler_list.add(mock_callback, 3)
    handler_list.add(mock_callback, 2)
    assert handler_list._list[0] == handler_list.Item(mock_callback, 1)
    assert handler_list._list[1] == handler_list.Item(mock_callback, 2)
    assert handler_list._list[2] == handler_list.Item(mock_callback, 3)

def test_handlerlist_add_multiple_with_same_priority():
    """Tests the list order from adding multiple items out of order with some items having the same priority."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1)
    handler_list.add(mock_callback, 5)
    handler_list.add(mock_callback, 2)
    handler_list.add(mock_wrong_callback, 2)
    assert handler_list._list[0] == handler_list.Item(mock_callback, 1)
    assert handler_list._list[1] == handler_list.Item(mock_callback, 2)
    assert handler_list._list[2] == handler_list.Item(mock_wrong_callback, 2)
    assert handler_list._list[3] == handler_list.Item(mock_callback, 5)

def test_handlerlist_len():
    """Tests the len function on a HandlerList."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1)
    handler_list.add(mock_callback, 2)
    assert len(handler_list) == 2

def test_handlerlist_remove():
    """Tests removing an item."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1)
    handler_list.add(mock_wrong_callback, 2)
    handler_list.remove(mock_callback)
    assert len(handler_list) == 1
    handler_list.remove(mock_wrong_callback)
    assert len(handler_list) == 0

def test_handlerlist_calling_handlers():
    """Tests calling handler functions in the HandlerList."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 0)
    handler_list.add(mock_wrong_callback, 1)
    assert handler_list[0]()
    assert not handler_list[1]()
    handler_list.add(mock_wrong_callback, 3)
    handler_list.add(mock_callback, 2)
    assert handler_list[2]()
    assert not handler_list[3]()

def test_handlerlist_iteration():
    """Tests iterating over HandlerList items and calling their functions."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1)
    handler_list.add(mock_callback, 2)
    handler_list.add(mock_callback, 3)
    calls = 0
    for function in handler_list:
        calls = calls + 1
        assert function()
    assert calls == 3
