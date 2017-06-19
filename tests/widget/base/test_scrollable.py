#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_scrollable.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       06/08/2017
#

"""
Unittests for nwid.widget.base.scrollable module.
"""

from __future__ import absolute_import

from nwid import Point, Size
from nwid.widget.base import Scrollable
import pytest


## Test Scrollable mixin ##

class MockScrollable(Scrollable):
    """A Mock of a scrollable object."""
    def __init__(self):
        self.size = Size(15, 15)
        self.offset = Point(5, 5)
        self.viewport = MockViewport()
        super(MockScrollable, self).__init__()

class MockViewport(object):
    """A Mock of an object with a viewport."""
    def __init__(self, height = 5, width = 5):
        self.size = Size(height, width)


def test_Scrollable_must_have_offset_property():
    """A Scrollable object must have an offset property."""
    class MockObject(Scrollable):
        """A Mock of a scrollable object."""
        def __init__(self):
            self.size = Size()
            self.viewport = MockViewport()
            super(MockObject, self).__init__()

    with pytest.raises(AttributeError):
        mock_scrollable = MockObject()

def test_Scrollable_must_have_size_property():
    """A Scrollable object must have a size property."""
    class MockObject(Scrollable):
        """A Mock of a scrollable object."""
        def __init__(self):
            self.offset = Point()
            self.viewport = MockViewport()
            super(MockObject, self).__init__()

    with pytest.raises(AttributeError):
        mock_scrollable = MockObject()

def test_Scrollable_must_have_viewport_property():
    """A Scrollable object must have a viewport property."""
    class MockObject(Scrollable):
        """A Mock of a scrollable object."""
        def __init__(self):
            self.size = Size()
            self.offset = Point()
            super(MockObject, self).__init__()

    with pytest.raises(AttributeError):
        mock_scrollable = MockObject()

def test_Scrollable_can_scroll_up_by_rows():
    """A Scrollable object can scroll up by rows."""
    scrollable = MockScrollable()
    scrollable.scroll_up()
    assert scrollable.offset.row == 4
    assert scrollable.offset.col == 5
    scrollable.scroll_up(2)
    assert scrollable.offset.row == 2
    assert scrollable.offset.col == 5

def test_Scrollable_cannot_scroll_up_with_no_vertical_scroll():
    """A Scrollable object cannot scroll up without vertical_scroll set."""
    scrollable = MockScrollable()
    scrollable.vertical_scroll = False
    scrollable.scroll_up()
    assert scrollable.offset.row == 5
    assert scrollable.offset.col == 5
    scrollable.scroll_up(2)
    assert scrollable.offset.row == 5
    assert scrollable.offset.col == 5

def test_Scrollable_has_a_highest_offset_property():
    """A Scrollable object has a highest offset property."""
    scrollable = MockScrollable()
    assert scrollable.highest_offset == 0

def test_Scrollable_cannot_scroll_up_above_top():
    """A Scrollable object cannot scroll up past the highest edge."""
    scrollable = MockScrollable()
    scrollable.scroll_up(5)
    assert scrollable.offset.row == 0
    scrollable.scroll_up(2)
    assert scrollable.offset.row == scrollable.highest_offset

def test_Scrollable_can_scroll_down_by_rows():
    """A Scrollable object can scroll down by rows."""
    scrollable = MockScrollable()
    scrollable.scroll_down()
    assert scrollable.offset.row == 6
    assert scrollable.offset.col == 5
    scrollable.scroll_down(2)
    assert scrollable.offset.row == 8
    assert scrollable.offset.col == 5

def test_Scrollable_cannot_scroll_down_with_no_vertical_scroll():
    """A Scrollable object cannot scroll down without vertical_scroll set."""
    scrollable = MockScrollable()
    scrollable.vertical_scroll = False
    scrollable.scroll_down()
    assert scrollable.offset.row == 5
    assert scrollable.offset.col == 5
    scrollable.scroll_down(2)
    assert scrollable.offset.row == 5
    assert scrollable.offset.col == 5

def test_Scrollable_has_a_lowest_offset_property():
    """A Scrollable object has a lowest offset property."""
    scrollable = MockScrollable()
    assert scrollable.lowest_offset == 10

def test_Scrollable_cannot_scroll_down_below_bottom():
    """A Scrollable object cannot scroll down past the lowest edge."""
    scrollable = MockScrollable()
    scrollable.scroll_down(5)
    assert scrollable.offset.row == 10
    scrollable.scroll_down(2)
    assert scrollable.offset.row == scrollable.lowest_offset

def test_Scrollable_can_scroll_left_by_cols():
    """A Scrollable object can scroll left by cols."""
    scrollable = MockScrollable()
    scrollable.scroll_left()
    assert scrollable.offset.row == 5
    assert scrollable.offset.col == 4
    scrollable.scroll_left(2)
    assert scrollable.offset.row == 5
    assert scrollable.offset.col == 2

def test_Scrollable_cannot_scroll_left_with_no_horizontal_scroll():
    """A Scrollable object cannot scroll left without horizontal_scroll set."""
    scrollable = MockScrollable()
    scrollable.horizontal_scroll = False
    scrollable.scroll_left()
    assert scrollable.offset.row == 5
    assert scrollable.offset.col == 5
    scrollable.scroll_left(2)
    assert scrollable.offset.row == 5
    assert scrollable.offset.col == 5

def test_Scrollable_has_a_leftmost_offset_property():
    """A Scrollable object has a leftmost offset property."""
    scrollable = MockScrollable()
    assert scrollable.leftmost_offset == 0

def test_Scrollable_cannot_scroll_left_past_left_edge():
    """A Scrollable object cannot scroll left past the leftmost edge."""
    scrollable = MockScrollable()
    scrollable.scroll_left(5)
    assert scrollable.offset.col == 0
    scrollable.scroll_left(2)
    assert scrollable.offset.col == scrollable.leftmost_offset

def test_Scrollable_can_scroll_right_by_cols():
    """A Scrollable object can scroll right by cols."""
    scrollable = MockScrollable()
    scrollable.scroll_right()
    assert scrollable.offset.row == 5
    assert scrollable.offset.col == 6
    scrollable.scroll_right(2)
    assert scrollable.offset.row == 5
    assert scrollable.offset.col == 8

def test_Scrollable_cannot_scroll_right_with_no_horizontal_scroll():
    """A Scrollable object cannot scroll right without horizontal_scroll set."""
    scrollable = MockScrollable()
    scrollable.horizontal_scroll = False
    scrollable.scroll_right()
    assert scrollable.offset.row == 5
    assert scrollable.offset.col == 5
    scrollable.scroll_right(2)
    assert scrollable.offset.row == 5
    assert scrollable.offset.col == 5

def test_Scrollable_has_a_rightmost_offset_property():
    """A Scrollable object has a rightmost offset property."""
    scrollable = MockScrollable()
    assert scrollable.rightmost_offset == 10

def test_Scrollable_cannot_scroll_right_past_right_edge():
    """A Scrollable object cannot scroll right past the rightmost edge."""
    scrollable = MockScrollable()
    scrollable.scroll_right(5)
    assert scrollable.offset.col == 10
    scrollable.scroll_right(2)
    assert scrollable.offset.col == scrollable.rightmost_offset
