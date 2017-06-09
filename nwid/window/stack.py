#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             window_stack.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/06/2016
#

"""
nwid.window.stack
~~~~~~~~~~~~~~~~~

This module contains the WindowStack object for managing multiple nwid windows.
"""

from __future__ import absolute_import

from nwid.exceptions import ExitNwidApp


class WindowStack(list):
    """Contains a stack of windows to be managed by an nwid app."""
    def __init__(self, parent_app=None):
        """Initializes the parent_app."""
        if not parent_app:
            raise Exception('A WindowStack must have a parent App object.')
        self._parent_app = parent_app
        self._window_list = []

    def __iter__(self):
        """Generator that yeilds windows from the list."""
        for window in self._window_list:
            yield window

    def append(self, window):
        """Appends a new window onto the top of the stack."""
        self._window_list.append(window)

    def pop(self):
        """Pops the topmost window off the stack."""
        if self._window_list:
            return self._window_list.pop()
        raise ExitNwidApp('No windows remain in stack.')

    @property
    def top(self):
        """Returns the top window of the stack.
        When no windows are left, it raises ExitNwidApp exception to close the app."""
        if not self._window_list:
            raise ExitNwidApp('No windows remain in stack.')
        return self._window_list[-1]
