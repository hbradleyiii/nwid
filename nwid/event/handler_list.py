#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             handler_list.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/06/2016
#

"""
nwid.event.handler_list
~~~~~~~~~~~~~~~~~~~~~~~~

The HandlerList is a list of one or more listeners on an object for one
particular event.

It allows an object to have more than one listener (with different priorities)
for the same event.
"""

from __future__ import absolute_import

from collections import namedtuple


# Propogation methods:
EVENT_BUBBLE  = 0   # Default for creating events (0 == False)
EVENT_CAPTURE = 1   # Default for triggering events

HandlerListItem = namedtuple('HandlerListItem', ['callback_func', 'priority',
                                             'identifier', 'method'])


class HandlerList(object):
    """A HandlerList is a list of one or more listeners on an object for one
    particular event.

    It defines an ordered list of a namedtuple (HandlerListItem) with a
    callback_func and priority.

    The list is ordered based off the priority with lower integers coming
    before higher integers. This list is intended to be used as the list of
    handlers on an object for one particular event.

    :param callback_func:
    :param priority:
    :param identifier:
    """

    def __init__(self, callback_func=None, priority=50, identifier=None,
                 method=EVENT_BUBBLE):
        """Initializes an empty list. Can optionally add an item at initialization."""
        self._list = []
        if callback_func:
            self.add(callback_func, priority, identifier, method)

    def __len__(self):
        """Returns the length of the list."""
        return len(self._list)

    def add(self, callback_func, priority=50, identifier=None,
            method=EVENT_BUBBLE):
        """Inserts item of (callback_func, priority) into the list based on priority."""
        new_item = HandlerListItem(callback_func, priority, identifier, method)
        for index, item in enumerate(self._list):
            if priority < item.priority:
                self._list = self._list[:index] + [new_item] + self._list[index:]
                break
        else:
            self._list.append(HandlerListItem(callback_func, priority, identifier,
                                        method))

    def remove(self, id_=None):
        """Removes (all) item(s) with callback_func.

        NOTE: You can add a callback function more than once, and it will be
        called for each time it is added. But if you remove it by the function,
        it will remove all occurences of it for that particular event.
        """

        if not id_:
            raise TypeError('HandlerList.remove() method must take either a callback_func or an identifier.')
        for item in self._list:
            if id_ in [item.identifier, item.callback_func]:
                self._list.remove(item)

    def with_method(self, method):
        """A generator for yeilding callback functions of a certain method."""
        for item in (items for items in self._list
                        if items.method == method):
            yield item.callback_func

    def __getitem__(self, index):
        """Returns _only_ the callback_func. Priority is only intended to be used internally."""
        return self._list[index].callback_func

    def __contains__(self, id_):
        return any(item.identifier == id_ for item in self._list) or \
               any(item.callback_func == id_ for item in self._list)
