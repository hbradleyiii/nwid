#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             coordinates.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/19/2016
#

"""
nwid.coordinates
~~~~~~~~~~~~~~~~

This module contains the Coordinates data structure.
"""

class Coordinates(object):
    """A Coordinates object represents the row and column of a screen position."""
    def __init__(self, row = 0, col = 0):
        """Initializes the row and col attributes."""
        self.row = row
        self.col = col

    def __str__(self):
        """Coordinates string."""
        return '(' + str(self.row) + ', ' + str(self.col) + ')'

    def __repr__(self):
        """Coordinates repr."""
        return 'Coordinates' + str(self)

    def __eq__(self, other):
        """Compares this object with another Coordinates object."""
        try:
            return self.row == other.row and self.col == other.col
        except AttributeError:  # Can also take a tuple (row, col)
            return self.row == other[0] and self.col == other[1]

    def __add__(self, other):
        """Adds either a Coordinates or a tuple of (row, col) to this object."""
        try:
            return Coordinates(self.row + other.row, self.col + other.col)
        except AttributeError:  # Can also take a tuple (row, col)
            return Coordinates(self.row + other[0], self.col + other[1])

    def __radd__(self, other):
        """Adds either a Coordinates or a tuple of (row, col) to this object."""
        return self.__add__(other)

    def __sub__(self, other):
        """Subtracts either a Coordinates or a tuple of (row, col) from this object."""
        try:
            return Coordinates(self.row - other.row, self.col - other.col)
        except AttributeError:  # Can also take a tuple (row, col)
            return Coordinates(self.row - other[0], self.col - other[1])

    def __rsub__(self, other):
        """Subtracts this object's row, col from either another Coordinates or
        a tuple of (row, col)."""
        try:
            return Coordinates(other.row - self.row, other.col - self.col)
        except AttributeError:  # Can also take a tuple (row, col)
            return Coordinates(other[0] - self.row, other[1] - self.col)
