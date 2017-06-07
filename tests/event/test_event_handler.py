#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_event_handler.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       06/03/2017
#

"""
Unittests for nwid.events.event_handler module.
"""

from __future__ import absolute_import

from nwid.event import EventHandler, EVENT_BUBBLE, EVENT_CAPTURE
import pytest


## Mock Functions/Classes ##

def mock_callback(_=None):
    Mock.mock_callback_was_called = True
    return True

def mock_alt_callback(_=None):
    Mock.mock_alt_callback_was_called = True
    return False

class Mock():
    mock_callback_was_called = False
    mock_alt_callback_was_called = False

def Mock_reset():
    Mock.mock_callback_was_called = False
    Mock.mock_alt_callback_was_called = False

class MockImplementationOfEventHandler(EventHandler):
    """Mock Implementation of an EventHandler."""
    def __init__(self, *args, **kwargs):
        super(MockImplementationOfEventHandler, self).__init__(*args, **kwargs)
        self._focused_child = None
        self._parent = None

    @property
    def focused_child(self):
        return self._focused_child

    @property
    def parent(self):
        return self._parent

    def has_child(self):
        return True if self._focused_child else False

    def has_parent(self):
        return True if self._parent else False

class MockCallback(object):
    def __init__(self):
        self.order = []

    def c1(self, _):
        self.order.append(1)

    def c2(self, _):
        self.order.append(2)

    def c3(self, _):
        self.order.append(3)

    def c4(self, _):
        self.order.append(4)

    def c5(self, _):
        self.order.append(5)

    def c6(self, _):
        self.order.append(6)

    def c7(self, _):
        self.order.append(7)

    def c8(self, _):
        self.order.append(8)


## Test mixin object EventHandler ##

def test_EventHandler_is_initialized_with_empty_dict():
    """An EventHandler is initialized with an empty collection of events
    mapped to each handler list."""
    event_handler = EventHandler()
    assert event_handler.events == {}

def test_EventHandler_can_register_a_new_event():
    """An EventHandler is initialized with an empty collection of events
    mapped to each handler list."""
    event_handler = EventHandler()
    event_handler.register('event', mock_callback)
    assert mock_callback in event_handler.events['event']

def test_EventHandler_can_register_multiple_callbacks_to_one_event():
    """An EventHandler can register more than one callback to a particular
    event."""
    event_handler = EventHandler()
    event_handler.register('event', mock_callback)
    event_handler.register('event', mock_alt_callback)
    assert mock_callback in event_handler.events['event']
    assert mock_callback in event_handler.events['event']

def test_EventHandler_can_unregister_an_event():
    """An EventHandler can unregister an event."""
    event_handler = EventHandler()
    event_handler.register('event', mock_callback)
    event_handler.register('event', mock_alt_callback)
    event_handler.unregister('event', mock_callback)
    assert mock_callback not in event_handler.events['event']
    assert mock_alt_callback in event_handler.events['event']
    event_handler.unregister('event', mock_alt_callback)
    assert mock_alt_callback not in event_handler.events['event']

def test_EventHandler_can_run_handlers_for_an_event_bubbling():
    Mock_reset()

    event_handler = EventHandler()
    event_handler.register('event', mock_callback)  # Using default method
    event_handler.register('event', mock_alt_callback, method=EVENT_BUBBLE)

    assert not event_handler.run_handlers('no_handlers', method=EVENT_BUBBLE)

    assert not Mock.mock_callback_was_called
    assert not Mock.mock_alt_callback_was_called

    event_handler.run_handlers('event', EVENT_BUBBLE)

    assert Mock.mock_callback_was_called
    assert Mock.mock_alt_callback_was_called

def test_EventHandler_can_run_handlers_for_an_event_capturing():
    Mock_reset()

    event_handler = EventHandler()
    event_handler.register('event', mock_callback, method=EVENT_CAPTURE)
    event_handler.register('event', mock_alt_callback, method=EVENT_CAPTURE)

    assert not Mock.mock_callback_was_called
    assert not Mock.mock_alt_callback_was_called

    event_handler.run_handlers('event', EVENT_CAPTURE)

    assert Mock.mock_callback_was_called
    assert Mock.mock_alt_callback_was_called

def test_EventHandler_can_trigger_an_event():
    Mock_reset()

    event_handler = EventHandler()
    event_handler.register('event', mock_callback, method=EVENT_CAPTURE)
    event_handler.register('event', mock_alt_callback, method=EVENT_BUBBLE)

    assert not Mock.mock_callback_was_called
    assert not Mock.mock_alt_callback_was_called

    event_handler.trigger('event')

    assert Mock.mock_callback_was_called
    assert Mock.mock_alt_callback_was_called

def test_EventHandler_can_trigger_an_event_on_children():
    Mock_reset()

    eh_parent = MockImplementationOfEventHandler()
    eh_child = MockImplementationOfEventHandler()
    eh_grandchild = MockImplementationOfEventHandler()

    eh_parent._focused_child = eh_child
    eh_child._focused_child = eh_grandchild

    eh_child._parent = eh_parent
    eh_grandchild._parent = eh_child

    eh_child.register('event', mock_callback)
    eh_grandchild.register('event', mock_alt_callback)

    assert not Mock.mock_callback_was_called
    assert not Mock.mock_alt_callback_was_called

    eh_parent.trigger('event')

    assert Mock.mock_callback_was_called
    assert Mock.mock_alt_callback_was_called

def test_EventHandler_can_bubble_events_up_to_parents():
    Mock_reset()

    eh_parent = MockImplementationOfEventHandler()
    eh_child = MockImplementationOfEventHandler()
    eh_grandchild = MockImplementationOfEventHandler()

    eh_parent._focused_child = eh_child
    eh_child._focused_child = eh_grandchild

    eh_child._parent = eh_parent
    eh_grandchild._parent = eh_child

    eh_child.register('event', mock_callback)
    eh_parent.register('event', mock_alt_callback)

    assert not Mock.mock_callback_was_called
    assert not Mock.mock_alt_callback_was_called

    eh_grandchild.trigger('event')

    assert Mock.mock_callback_was_called
    assert Mock.mock_alt_callback_was_called

def test_EventHandler_triggers_events_in_proper_order():
    """The EventHandler should trigger events in order.
    First, it starts with the object that was triggered firing its capture
    events. Then each child in turn fires its capture events. After firing its
    capture events, the last child then fires its bubble events. Then each
    parent in turn fires their own capture events starting with the immediate
    parent and working until there are no more parents."""
    Mock_reset()

    eh_grandparent = MockImplementationOfEventHandler()
    eh_parent = MockImplementationOfEventHandler()
    eh_child = MockImplementationOfEventHandler()
    eh_grandchild = MockImplementationOfEventHandler()

    eh_grandparent._focused_child = eh_parent
    eh_parent._focused_child = eh_child
    eh_child._focused_child = eh_grandchild

    eh_parent._parent = eh_grandparent
    eh_child._parent = eh_parent
    eh_grandchild._parent = eh_child

    callback = MockCallback()

    # Should not fire:
    eh_grandparent.register('event', callback.c8, method=EVENT_CAPTURE)

    # Should fire in this order:
    eh_parent.register('event', callback.c1, method=EVENT_CAPTURE)
    eh_child.register('event', callback.c2, method=EVENT_CAPTURE)
    eh_grandchild.register('event', callback.c3, method=EVENT_CAPTURE)
    eh_grandchild.register('event', callback.c4)  # Default (BUBBLE)
    eh_child.register('event', callback.c5, method=EVENT_BUBBLE)
    eh_parent.register('event', callback.c6, method=EVENT_BUBBLE)
    eh_grandparent.register('event', callback.c7, method=EVENT_BUBBLE)

    eh_parent.trigger('event')

    assert callback.order == [1, 2, 3, 4, 5, 6, 7]

def test_EventHandler_by_default_has_no_children():
    """An EventHandler has no children by default. It's subclasses must
    implement them."""
    event_handler = EventHandler()
    assert event_handler.has_child() == False
    with pytest.raises(NotImplementedError):
        event_handler.focused_child

def test_EventHandler_by_default_has_no_parent():
    """An EventHandler has no children by default. It's subclasses must
    implement them."""
    event_handler = EventHandler()
    assert event_handler.has_parent() == False
    with pytest.raises(NotImplementedError):
        event_handler.parent
