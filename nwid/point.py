#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             point.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/19/2016
#

"""
nwid.point
~~~~~~~~~~

This module contains the Point data structure.
"""

class Point(object):
    """A Point object represents the row and column of a screen position."""
    def __init__(self, row = 0, col = 0):
        """Initializes the row and col attributes."""
        self.row = row
        self.col = col

    def __str__(self):
        """Point string."""
        return '(' + str(self.row) + ', ' + str(self.col) + ')'

    def __repr__(self):
        """Point repr."""
        return 'Point' + str(self)

    def __eq__(self, other):
        """Compares this object with another Point object."""
        try:
            return self.row == other.row and self.col == other.col
        except AttributeError:  # Can also take a tuple (row, col)
            return self.row == other[0] and self.col == other[1]

    def __add__(self, other):
        """Adds either a Point or a tuple of (row, col) to this object."""
        try:
            return Point(self.row + other.row, self.col + other.col)
        except AttributeError:  # Can also take a tuple (row, col)
            return Point(self.row + other[0], self.col + other[1])

    def __radd__(self, other):
        """Adds either a Point or a tuple of (row, col) to this object."""
        return self.__add__(other)

    def __sub__(self, other):
        """Subtracts either a Point or a tuple of (row, col) from this object."""
        try:
            return Point(self.row - other.row, self.col - other.col)
        except AttributeError:  # Can also take a tuple (row, col)
            return Point(self.row - other[0], self.col - other[1])

    def __rsub__(self, other):
        """Subtracts this object's row, col from either another Point or
        a tuple of (row, col)."""
        try:
            return Point(other.row - self.row, other.col - self.col)
        except AttributeError:  # Can also take a tuple (row, col)
            return Point(other[0] - self.row, other[1] - self.col)

    @property
    def rows(self):
        """A symantic alias for referring to 'number of rows' vs 'row number'."""
        return self.row

    @rows.setter
    def rows(self, row):
        """A symantic alias for setting 'number of rows' vs. 'row number'."""
        self.row += row

    @property
    def cols(self):
        """A symantic alias for referring to 'number of cols' vs. 'col number'."""
        return self.col

    @cols.setter
    def cols(self, col):
        """A symantic alias for setting 'number of cols' vs. 'col number'."""
        self.col += col

    @property
    def y(self):
        """A symantic alias for referring to 'y' row."""
        return self.row

    @y.setter
    def y(self, y):
        """A symantic alias for setting 'y' row."""
        self.row += y

    @property
    def x(self):
        """A symantic alias for referring to 'x' column."""
        return self.col

    @x.setter
    def x(self, x):
        """A symantic alias for setting 'x' row."""
        self.col += x
