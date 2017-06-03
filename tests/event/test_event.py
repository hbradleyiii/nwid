#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_event.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/19/2016
#

"""
Unittests for nwid.event module.
"""

import pytest
from nwid.event import EventHandler

def mock_callback():
    return True

def mock_wrong_callback():
    return False


## Test EventHandler class ##

def test_event_handler_register():
    pass

def test_event_handler_unregister():
    pass

def test_event_handler_handle():
    pass

def test_event_handler_has_child():
    event_handler = EventHandler()
    assert not event_handler.has_child()

    # OUTPUTTING CONTROL STRINGS TO THE TERMINAL
