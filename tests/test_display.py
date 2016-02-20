#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_events.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/19/2016
#

"""
Unittests for nwid.display module.
"""

from nwid import Coordinates


## Test data structure Coordinates ##

def test_coordinates_initialize():
    """Tests initializing a Coordinates object."""
    coordinates = Coordinates(10, 5)
    assert coordinates.x == 10
    assert coordinates.y == 5

def test_coordinates_string():
    """Tests a Coordinates object string method."""
    coordinates = Coordinates(10, 5)
    assert str(coordinates) == '(10, 5)'

def test_coordinates_repr():
    """Tests a Coordinates object repr method."""
    coordinates = Coordinates(10, 5)
    assert repr(coordinates) == 'Coordinates(10, 5)'

def test_coordinates_equality():
    """Tests a Coordinates object equality method."""
    position1 = Coordinates(10, 5)
    position2 = Coordinates(10, 5)
    position3 = Coordinates(15, 8)
    assert position1 == position2
    assert position2 == position1
    assert position1 != position3
    assert position3 == Coordinates(15, 8)
    assert position3 == (15, 8)

def test_coordinates_addition():
    """Tests a Coordinates object addition method."""
    position1 = Coordinates(10, 1)
    position2 = Coordinates(10, 2)
    position3 = Coordinates(20, 3)
    assert position1 + position2 == Coordinates(20, 3)
    assert position1 + position2 == position3
    assert position1 + (10, 2) == position3
    assert (10, 1) + position2 == position3

def test_coordinates_subtraction():
    """Tests a Coordinates object subtraction method."""
    position1 = Coordinates(10, 5)
    position2 = Coordinates(5, 2)
    position3 = Coordinates(5, 3)
    assert position1 - position2 == Coordinates(5, 3)
    assert position1 - position2 == position3
    assert position1 - (5, 2) == position3
    assert (10, 5) - position2 == position3
