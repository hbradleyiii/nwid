#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             event.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/06/2016
#

"""
nwid.event.event
~~~~~~~~~~~~~~~~

This module contains the event object.
"""

class Event(object):
    """This class describes an event."""
    def __init__(self, name, cursor_pos=(0, 0), args=None):
        """Initializes an event object.

        The event name is a string representing the event. For single character
        keyboard events, it is simply a one-character string of the letter,
        number, or symbol.  Other events, such as a window resize are a
        representative string ('SIGWINCH').

        :param name: A string representing the event.
        :param cursor_pos: A Coordinates object representing the cursor
            position when the event was fired.
        """
        self.name = name
        self.cursor_pos = cursor_pos
        self.args = args

    def __repr__(self):
        """Returns a python string that evaluates to the object instance."""
        return "Event({0}, {1}, {2})".format(self.name, self.self.cursor_pos, self.args)

    def __str__(self):
        """Returns the name of the event"""
        if len(self.name) == 1:
            return 'KEY: ' + self.name
        return self.name
