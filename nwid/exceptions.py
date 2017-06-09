#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             exceptions.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/06/2016
#

"""
nwid.exceptions
~~~~~~~~~~~~~~~

This module contains the exceptions for the nwid package.
"""

class ExitNwidApp(Exception):
    """Exception used to exit App's event loop."""

class PreventDefault(Exception):
    """An exception that is used to prevent event propagation."""

class RunCallbackCloseWindow(Exception):
    """Exception used to exit App's event loop."""

class CloseWindow(Exception):
    """Exception used to exit App's event loop."""



class WindowNotBound(Exception):
    """ """

class OutOfBounds(Exception):
    """ """
