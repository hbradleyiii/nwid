#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_handler_list.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/19/2016
#

"""
Unittests for nwid.events.handler_list module.
"""

from __future__ import absolute_import

from nwid.event import EVENT_BUBBLE, EVENT_CAPTURE, HandlerList
import pytest


def mock_callback():
    return True

def mock_alt_callback():
    return False


## Test data structure HandlerList ##

def test_HandlerList_can_be_initialized_with_an_item():
    """A HandlerList can be initialized with an item."""
    handler_list = HandlerList(mock_callback, 1)
    assert handler_list._list[0] == handler_list.Item(mock_callback, 1, None,
                                                      False)

def test_HandlerList_can_have_items_added():
    """A HandlerList can have items added using the 'add' method."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1)
    assert handler_list._list[0] == handler_list.Item(mock_callback, 1, None,
                                                      False)

def test_HandlerList_can_add_multiple_items():
    """A HanlderList should be able to hold multiple items and should respect
    the order in which items were added."""
    handler_list = HandlerList()
    handler_list.add(mock_callback)
    handler_list.add(mock_callback)
    handler_list.add(mock_callback)
    assert handler_list._list[0] == handler_list.Item(mock_callback, 50, None,
                                                      False)
    assert handler_list._list[1] == handler_list.Item(mock_callback, 50, None,
                                                      False)
    assert handler_list._list[2] == handler_list.Item(mock_callback, 50, None,
                                                      False)

def test_HandlerList_can_add_multiple_items_with_priorities():
    """A HanlderList should be able to hold multiple items and should respect
    their priorities."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 3)
    handler_list.add(mock_callback, 1)
    handler_list.add(mock_callback, 2)
    assert handler_list._list[0] == handler_list.Item(mock_callback, 1, None,
                                                      False)
    assert handler_list._list[1] == handler_list.Item(mock_callback, 2, None,
                                                      False)
    assert handler_list._list[2] == handler_list.Item(mock_callback, 3, None,
                                                      False)

def test_HandlerList_can_add_multiple_items_with_some_having_same_priority():
    """A HandlerList should be able to handle adding multiple items with some
    having the same priority. The order when priority is the same is just the
    order of execution."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1)
    handler_list.add(mock_callback, 5)
    handler_list.add(mock_callback, 2)
    handler_list.add(mock_alt_callback, 2)
    assert handler_list._list[0] == handler_list.Item(mock_callback, 1, None,
                                                      False)
    assert handler_list._list[1] == handler_list.Item(mock_callback, 2, None,
                                                      False)
    assert handler_list._list[2] == handler_list.Item(mock_alt_callback, 2,
                                                      None, False)
    assert handler_list._list[3] == handler_list.Item(mock_callback, 5, None,
                                                      False)

def test_HandlerList_can_add_items_without_a_priority():
    """A HandlerList can add items without a priority. (It defaults to 50)."""
    handler_list = HandlerList()
    handler_list.add(mock_callback)
    handler_list.add(mock_callback)
    assert handler_list._list[0].priority == 50
    assert handler_list._list[1].priority == 50

def test_HandlerList_can_add_items_with_an_identifier():
    """A HandlerList can add items with a string identifier."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1, 'first-item')
    handler_list.add(mock_callback, 2, 'second-item')
    assert handler_list._list[0].identifier == 'first-item'
    assert handler_list._list[1].identifier == 'second-item'

def test_HandlerList_can_add_items_with_a_propagation_type():
    """A HandlerList can add items with a propagation type."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1, propagation=EVENT_CAPTURE)
    handler_list.add(mock_callback, 2, propagation=EVENT_BUBBLE)
    handler_list.add(mock_callback, 3, propagation=True)
    handler_list.add(mock_callback, 4, propagation=False)
    assert handler_list._list[0].propagation == EVENT_CAPTURE
    assert handler_list._list[1].propagation == EVENT_BUBBLE
    assert handler_list._list[2].propagation == True
    assert handler_list._list[3].propagation == False

def test_HandlerList_can_tell_its_len():
    """A HandlerList should be able to return its length."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1)
    handler_list.add(mock_callback, 2)
    assert len(handler_list) == 2

def test_HandlerList_can_remove_items_by_identifier():
    """A HandlerList can remove items once added."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1, 'first-item')
    handler_list.add(mock_alt_callback, 2, 'second-item')
    assert len(handler_list) == 2
    handler_list.remove('first-item')
    assert len(handler_list) == 1
    handler_list.remove('second-item')
    assert len(handler_list) == 0

def test_HandlerList_can_remove_items_by_callback():
    """A HandlerList can remove items once added."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1)
    handler_list.add(mock_alt_callback, 2)
    assert len(handler_list) == 2
    handler_list.remove(mock_callback)
    assert len(handler_list) == 1
    handler_list.remove(mock_alt_callback)
    assert len(handler_list) == 0

def test_HandlerList_callbacks_are_functions_that_can_be_called():
    """A HandlerList callback is a function that can be called."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 0)
    handler_list.add(mock_alt_callback, 1)
    assert handler_list[0]()
    assert not handler_list[1]()
    handler_list.add(mock_alt_callback, 3)
    handler_list.add(mock_callback, 2)
    assert handler_list[2]()
    assert not handler_list[3]()

def test_HandlerList_can_be_iterated_over():
    """A HandlerList can be iterated over (looped through)."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1)
    handler_list.add(mock_callback, 2)
    handler_list.add(mock_callback, 3)
    calls = 0
    for function in handler_list:
        calls = calls + 1
        assert function()  # Should return true
    assert calls == 3  # and should have been called 3 times

def test_HandlerList_can_test_for_existance_of_identifier():
    """A HandlerList can use 'in' to test if an identifier is in the list."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1, 'id')
    handler_list.add(mock_callback, 1, 'abc')
    assert 'id' in handler_list
    assert 'abc' in handler_list
    assert 'xyz' not in handler_list

def test_HandlerList_can_test_for_existance_of_function():
    """A HandlerList can use 'in' to test if a callback function is in the list."""
    handler_list = HandlerList()
    handler_list.add(mock_callback, 1, 'id')
    assert mock_callback in handler_list
    assert mock_alt_callback not in handler_list
    handler_list.add(mock_alt_callback, 1, 'abc')
    assert mock_alt_callback in handler_list
