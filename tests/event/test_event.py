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

from __future__ import absolute_import

from nwid.event import Event, event, FiredEvent


## Test Event object ##

test_event = Event('MY_EVENT', 'abc', 'keyboard')

def test_Event_has_a_name():
    assert test_event.name == 'MY_EVENT'

def test_Event_has_a_value():
    assert test_event.value == 'abc'

def test_Event_can_have_a_type():
    assert test_event.type == 'keyboard'


## Test FiredEvent object ##

test_fired_event = FiredEvent(test_event, (0, 0), 'other')

def test_FiredEvent_has_a_name():
    assert test_fired_event.name == 'MY_EVENT'

def test_FiredEvent_has_a_value():
    assert test_fired_event.value == 'abc'

def test_FiredEvent_can_have_a_type():
    assert test_fired_event.type == 'keyboard'

def test_FiredEvent_has_a_cursor_position():
    assert test_fired_event.cursor_pos == (0, 0)

def test_FiredEvent_can_have_other_args():
    assert test_fired_event.args == 'other'


## Test event dict ##

def test_event_dict_contains_an_Event():
    assert event['KEY_UP'].value == '\x1b[A'
    assert event['KEY_UP'].type == 'keyboard'
    assert event['KEY_UP'].name == 'KEY_UP'
