#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_point.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/19/2016
#

"""
Unittests for nwid.point module.
"""

from nwid import Point


## Test data structure Point ##

def test_Point_can_be_initialized_without_args():
    """A Point object can be initialized without any arguments."""
    point = Point()
    assert point.row == 0
    assert point.col == 0

def test_Point_can_be_initialized_with_rows_and_cols():
    """A Point object can be initialized with rows and cols."""
    point = Point(10, 5)
    assert point.row == 10
    assert point.col == 5

def test_Point_can_be_set_individually():
    """A Point object can have its (row, col) set individually."""
    point = Point()
    point.row = 20
    point.col = 30
    assert point.row == 20
    assert point.col == 30

def test_Point_has_a_string_representation_of_itself():
    """A Point object has a string representation of itself
    '(row, col)'."""
    point = Point(10, 5)
    assert str(point) == '(10, 5)'

def test_Point_repr():
    """Tests a Point object repr method."""
    point = Point(10, 5)
    assert repr(point) == 'Point(10, 5)'

def test_Point_can_be_compared_for_equality_equality():
    """A Point object can be compared with another for equality."""
    position1 = Point(10, 5)
    position2 = Point(10, 5)
    position3 = Point(15, 8)
    assert position1 == position2
    assert position2 == position1
    assert position1 != position3
    assert position3 == Point(15, 8)
    assert position3 == (15, 8)

def test_Point_can_be_added_to_another_Point():
    """A Point object can be added to another Point object."""
    position1 = Point(10, 1)
    position2 = Point(10, 2)
    position3 = Point(20, 3)
    assert position1 + position2 == Point(20, 3)
    assert position1 + position2 == position3

def test_Point_can_be_added_to_a_tuple():
    """A Point object can be added to a tuple of (row, col)."""
    position1 = Point(10, 1)
    position2 = Point(10, 2)
    position3 = Point(20, 3)
    assert position1 + (10, 2) == position3
    assert (10, 1) + position2 == position3

def test_Point_can_be_subtracted_from_another_Point():
    """A Point object can be subtracted from another Point object."""
    position1 = Point(10, 5)
    position2 = Point(5, 2)
    position3 = Point(5, 3)
    assert position1 - position2 == Point(5, 3)
    assert position1 - position2 == position3

def test_Point_can_be_subtracted_from_a_tuple():
    """A Point object can be subtracted from a tuple of (row, col)."""
    position1 = Point(10, 5)
    position2 = Point(5, 2)
    position3 = Point(5, 3)
    assert position1 - (5, 2) == position3
    assert (10, 5) - position2 == position3

def test_Point_can_be_referenced_by_plural_attributes():
    """A Point object can be referenced by its plural attributes (rows,
    cols)."""
    point = Point(10, 5)
    assert point.rows == 10
    assert point.cols == 5
    assert point.rows == point.row
    assert point.cols == point.col

def test_Point_can_be_set_by_plural_attributes():
    """A Point object can be set by its plural attributes (rows,
    cols)."""
    point = Point()
    point.rows = 10
    point.cols = 5
    assert point.row == 10
    assert point.col == 5

def test_Point_can_be_referenced_by_width_and_height_attributes():
    """A Point object can be referenced by its width and height attributes."""
    point = Point(10, 5)
    assert point.width == 5
    assert point.height == 10
    assert point.width == point.col
    assert point.height == point.row

def test_Point_can_be_set_by_width_and_height_attributes():
    """A Point object can be set by its width and height attributes."""
    point = Point()
    point.width = 10
    point.height = 5
    assert point.width == 10
    assert point.height == 5
