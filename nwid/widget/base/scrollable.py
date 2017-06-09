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

This module contains the Scrollable mixin object that describes an object that
can be scrolled.
"""

from __future__ import absolute_import


class Scrollable(object):
    """TODO"""

    def __init__(self, text, *attributes):
        self.text = text
        self.strings

        self.alignment = 0  # TODO:
        self.overflow = 0 # visible, scroll-X, scroll-Y, scroll, auto

    def scroll_up(self, lines=1):
        pass

    def scroll_down(self, lines=1):
        pass

    def scroll_left(self, chars=1):
        pass

    def scroll_right(self, chars=1):
        pass
