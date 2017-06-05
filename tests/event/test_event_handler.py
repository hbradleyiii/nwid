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

from mock import patch
from nwid.event import EventHandler
import pytest


def mock_callback():
    return True

def mock_alt_callback():
    return False


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
    assert event_handler.events['event'].callback_func == mock_callback

def test_EventHandler_can_register_multiple_callbacks_to_one_event():
    """An EventHandler can register more than one callback to a particular
    event."""
    event_handler = EventHandler()
    event_handler.register('event', mock_callback)
    assert event_handler.events['event'] == mock_callback
