#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_coordinates.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/19/2016
#

"""
Unittests for nwid.coordinates module.
"""

from nwid import Coordinates


## Test data structure Coordinates ##

def test_Coordinates_can_be_initialized_without_args():
    """A Coordinates object can be initialized without any arguments."""
    coordinates = Coordinates()
    assert coordinates.row == 0
    assert coordinates.col == 0

def test_Coordinates_can_be_initialized_with_rows_and_cols():
    """A Coordinates object can be initialized with rows and cols."""
    coordinates = Coordinates(10, 5)
    assert coordinates.row == 10
    assert coordinates.col == 5

def test_Coordinates_can_be_set_individually():
    """A Coordinates object can have its (row, col) set individually."""
    coordinates = Coordinates()
    coordinates.row = 20
    coordinates.col = 30
    assert coordinates.row == 20
    assert coordinates.col == 30

def test_Coordinates_has_a_string_representation_of_itself():
    """A Coordinates object has a string representation of itself
    '(row, col)'."""
    coordinates = Coordinates(10, 5)
    assert str(coordinates) == '(10, 5)'

def test_Coordinates_repr():
    """Tests a Coordinates object repr method."""
    coordinates = Coordinates(10, 5)
    assert repr(coordinates) == 'Coordinates(10, 5)'

def test_Coordinates_can_be_compared_for_equality_equality():
    """A Coordinates object can be compared with another for equality."""
    position1 = Coordinates(10, 5)
    position2 = Coordinates(10, 5)
    position3 = Coordinates(15, 8)
    assert position1 == position2
    assert position2 == position1
    assert position1 != position3
    assert position3 == Coordinates(15, 8)
    assert position3 == (15, 8)

def test_Coordinates_can_be_added_to_another_Coordinates():
    """A Coordinates object can be added to another Coordinates object."""
    position1 = Coordinates(10, 1)
    position2 = Coordinates(10, 2)
    position3 = Coordinates(20, 3)
    assert position1 + position2 == Coordinates(20, 3)
    assert position1 + position2 == position3

def test_Coordinates_can_be_added_to_a_tuple():
    """A Coordinates object can be added to a tuple of (row, col)."""
    position1 = Coordinates(10, 1)
    position2 = Coordinates(10, 2)
    position3 = Coordinates(20, 3)
    assert position1 + (10, 2) == position3
    assert (10, 1) + position2 == position3

def test_Coordinates_can_be_subtracted_from_another_Coordinates():
    """A Coordinates object can be subtracted from another Coordinates object."""
    position1 = Coordinates(10, 5)
    position2 = Coordinates(5, 2)
    position3 = Coordinates(5, 3)
    assert position1 - position2 == Coordinates(5, 3)
    assert position1 - position2 == position3

def test_Coordinates_can_be_subtracted_from_a_tuple():
    """A Coordinates object can be subtracted from a tuple of (row, col)."""
    position1 = Coordinates(10, 5)
    position2 = Coordinates(5, 2)
    position3 = Coordinates(5, 3)
    assert position1 - (5, 2) == position3
    assert (10, 5) - position2 == position3

def test_Coordinates_can_be_referenced_by_plural_attributes():
    """A Coordinates object can be referenced by its plural attributes (rows,
    cols)."""
    coordinates = Coordinates(10, 5)
    assert coordinates.rows == 10
    assert coordinates.cols == 5
    assert coordinates.rows == coordinates.row
    assert coordinates.cols == coordinates.col

def test_Coordinates_can_be_set_by_plural_attributes():
    """A Coordinates object can be set by its plural attributes (rows,
    cols)."""
    coordinates = Coordinates()
    coordinates.rows = 10
    coordinates.cols = 5
    assert coordinates.row == 10
    assert coordinates.col == 5

def test_Coordinates_can_be_referenced_by_x_y_attributes():
    """A Coordinates object can be referenced by its x/y attributes (x, y)."""
    coordinates = Coordinates(10, 5)
    assert coordinates.x == 5
    assert coordinates.y == 10
    assert coordinates.x == coordinates.col
    assert coordinates.y == coordinates.row

def test_Coordinates_can_be_set_by_x_y_attributes():
    """A Coordinates object can be set by its x/y attributes (x, y)."""
    coordinates = Coordinates()
    coordinates.y = 10
    coordinates.x = 5
    assert coordinates.row == 10
    assert coordinates.col == 5
