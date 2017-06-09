#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             event_handler.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       06/02/2017
#

"""
nwid.event
~~~~~~~~~~

The event handler is a mixin to be exteneded by an object that should be able
to handle events.
"""


from __future__ import absolute_import

from .handler_list import EVENT_BUBBLE, EVENT_CAPTURE, HandlerList


class EventHandler(object):
    """This class defines an object that can handle events.
    It is intended to be extended by a widget like object.
    """

    def __init__(self, *args, **kwargs):
        """Initializes an empty collection of events."""
        self.events = {}

    def register(self, event_name, callback_func, priority=50, identifier=None,
                method=EVENT_BUBBLE):
        """Registers an event with a callback function on this widget.
        An event may have more than one callback function in an ordered list
        arranged by priority.

        Events are mapped to a HandlerList in the dict self.events

        :param event_name: The name of the event.
        :param callback_func: A callback function. It must take exactly one
            argument. (the event object)
        :param priority: The order of priority for event handlers. Takes an
            integer (by convention 0-99).  0 will be called first and 99 is
            called last. This defaults to 50. Callbacks with the same priority
            will be run in the order in which they were originally registered.
        :param identifier: An optional string identifier for the event.
        """
        if event_name in self.events:
            self.events[event_name].add(callback_func, priority, identifier,
                                        method)
        else:
            self.events[event_name] = HandlerList(callback_func, priority,
                                                  identifier, method)

    def unregister(self, event_name, callback_func=None, identifier=None):
        """Unregisters an event handler.

        If a callback_func is given, only the callback_func attached to the
        event is removed. Otherwise, all handlers for that particular event are
        removed.

        :param event_name: The name of the event.
        :param callback_func: A callback function. It must take exactly one
            argument. (the event object)
        :param identifier: The identifier of the handler to unregister.
        """
        if callback_func:
            self.events[event_name].remove(callback_func)
        else:
            del self.events[event_name]

    def run_handlers(self, event, method=EVENT_CAPTURE):
        """Runs all callbacks for events with the passed propagation method."""
        if event not in self.events:
            return None
        for handler in self.events[str(event)].with_method(method):
            handler(event)

    # TODO, event passed here should be an event object NOT a string.

    def trigger(self, event=None, method=EVENT_CAPTURE):
        """Called to handle events that have been fired.

        If the (propagation) method flag is set to EVENT_CAPTURE, this function
        will run any handler for the event that has the method flag set to
        EVENT_CAPTURE. Then, if the object has children, it will trigger the
        event with the EVENT_CAPTURE flag on the focused child object.

        If it doesn't have children, it will run any handler for the event that
        has the method flag set to EVENT_BUBBLE. Then, if the object has a
        parent, it will trigger the event with the EVENT_BUBBLE flag on the
        parent.

        If this method is called with the method flag set to EVENT_BUBBLE,
        the EVENT_CAPTURE method is skipped. After the last parent, the

        Note that the propagation can be stopped by any of the handlers by
        raising the PreventDefault Exception (although this should be used
        sparingly).

        :param event: An object representing the event that occurred.
        """

        # Event Capturing
        if method == EVENT_CAPTURE:
            self.run_handlers(event, EVENT_CAPTURE)

            # Let children capture the event
            if self.has_child():
                self.focused_child.trigger(event, EVENT_CAPTURE)

            else: # At the last child, start the bubbling
                self.trigger(event, EVENT_BUBBLE)

        # Event Bubbling
        else:
            self.run_handlers(event, EVENT_BUBBLE)

            # Let the event bubble to the parents
            if self.has_parent():
                self.parent.trigger(event, EVENT_BUBBLE)

    def has_child(self):
        """This is a stub that implies the class cannot have children.
        If the class has children, this should method be implemented by the class."""
        return False

    def has_parent(self):
        """This is a stub that implies the class cannot have a parent.
        If the class has a parent, this should method be implemented by the class."""
        return False

    @property
    def focused_child(self):
        """This property must be implemented by subclasses that can have
        children."""
        raise NotImplementedError('Property must be implemented by subclass \
                                  of EventHandler.')

    @property
    def parent(self):
        """This property must be implemented by subclasses that can have
        children/parents."""
        raise NotImplementedError('Property must be implemented by subclass \
                                  of EventHandler.')
