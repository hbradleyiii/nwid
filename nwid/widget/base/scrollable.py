#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             scrollable.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       06/08/2017
#

"""
nwid.widget.base.scrollable
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the Scrollable mixin object that describes a buffer that
can be scrolled.

Assumptions:
    Objects that inherit Scrollable must have these attributes/properties:

        self.offset - This is the property that the Scrollable mixin works on.
            It is the point where the top right corner of the viewport overlaps
            with the LineBufferuffer.
        self.size - This is the size of the LineBuffer.
        self.viewport.size - This is the size of the viewport.

        +--LineBuffer-----------------------+
        |                                   |
        | offset                            |
        |   |                               |
        |   v                               |
        |   +-Viewport---+                  |
        |   |            |                  |
        |   |            |                  |
        |   +------------+ <- viewport.size |
        +-----------------------------------+ <- size

        Note: The viewport can be larger, smaller, or exactly the same size as the
        LineBuffer.
"""

from __future__ import absolute_import


class Scrollable(object):
    """Scrollable is a mixin that allows scrolling a LineBuffer's Viewport by
    changing its offset."""

    def __init__(self, horizontal_scroll = True, vertical_scroll = True ):
        """Initializes a Scrollable object.

        Assumes an offset Point, a size Size, and a Viewport Size."""

        self.vertical_scroll = horizontal_scroll
        self.horizontal_scroll = vertical_scroll

        try:
            self.offset.row
            self.offset.col
        except AttributeError:
            raise AttributeError('A Scrollable object must have an offset \
                            attribute that is a Point object.')

        try:
            self.size.height
            self.size.width
        except AttributeError:
            raise AttributeError('A Scrollable object must have a size attribute \
                            that is a Point object.')

        try:
            self.viewport.size.height
            self.viewport.size.width
        except AttributeError:
            raise AttributeError('A Scrollable object must have a viewport attribute \
                            that is a Viewport object.')

    def register_events(self):
        """TODO: """
        pass

    def scroll_up(self, rows=1):
        """Scrolls up."""
        if not self.vertical_scroll:
            return

        if self.offset.row - rows <= self.highest_offset:
            # Don't overscroll, just scroll to the top
            self.offset.row = self.highest_offset
        else:
            self.offset.row -= rows

    def scroll_down(self, rows=1):
        """Scrolls down."""
        if not self.vertical_scroll:
            return

        if self.offset.row + rows >= self.lowest_offset:
            # Don't overscroll, just scroll to the bottom
            self.offset.row = self.lowest_offset
        else:
            self.offset.row += rows

    def scroll_left(self, cols=1):
        """Scrolls left."""
        if not self.horizontal_scroll:
            return

        if self.offset.col - cols <= self.leftmost_offset:
            # Don't overscroll, just scroll to the far left
            self.offset.col = self.leftmost_offset
        else:
            self.offset.col -= cols

    def scroll_right(self, cols=1):
        """Scrolls right."""
        if not self.horizontal_scroll:
            return

        if self.offset.col + cols >= self.rightmost_offset:
            # Don't overscroll, just scroll to the far right
            self.offset.col = self.rightmost_offset
        else:
            self.offset.col += cols

    @property
    def highest_offset(self):
        """The highest offset value that can be scrolled to."""
        return 0

    @property
    def lowest_offset(self):
        """The lowest offset value that can be scrolled to."""
        return self.size.height - self.viewport.size.height

    @property
    def leftmost_offset(self):
        """The leftmost offset value that can be scrolled to."""
        return 0

    @property
    def rightmost_offset(self):
        """The rightmost offset value that can be scrolled to."""
        return self.size.width - self.viewport.size.width
