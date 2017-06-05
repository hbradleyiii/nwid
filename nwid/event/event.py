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

This module contains the Event object, the event dict, and the FiredEvent
object that contains a fired event and its context.
"""

from __future__ import absolute_import

from collections import namedtuple
import signal


Event = namedtuple('Event', ['name', 'value', 'type'])

class FiredEvent(object):
    """This object represents a fired event with its appropriate context."""
    def __init__(self, event, cursor_pos=(0, 0), args=None):
        """Initializes an event object.

        The event name is a string representing the event. For single character
        keyboard events, it is simply a one-character string of the letter,
        number, or symbol.  Signals, such as a window resize are a
        representative string ('SIGWINCH').

        :param event: An Event named tuple representing the event.
        :param cursor_pos: A Coordinates object representing the cursor
            position when the event was fired.
        """
        self.event = event
        self.cursor_pos = cursor_pos
        self.args = args

    def __repr__(self):
        """Returns a python string that evaluates to the object instance."""
        return "Event({0}, {1}, {2})".format(self.event, self.self.cursor_pos, self.args)

    def __str__(self):
        """Returns the name of the event"""
        return self.name

    @property
    def name(self):
        """An alias to the Event name property."""
        return self.event.name

    @property
    def value(self):
        """An alias to the Event value property."""
        return self.event.value

    @property
    def type(self):
        """An alias to the Event type property."""
        return self.event.type


_events = {

    'signal' : {
        'SIGCONT': signal.SIGCONT,
        'SIGWINCH': signal.SIGWINCH,
    },

    'keyboard' : {
        'KEY_ESCAPE': '\x1b',

        'KEY_UP': '\x1b[A',
        'KEY_DOWN': '\x1b[B',
        'KEY_RIGHT': '\x1b[C',
        'KEY_LEFT': '\x1b[D',

        'KEY_A': ord('A'),
        'KEY_B': ord('B'),
        'KEY_C': ord('C'),
        'KEY_D': ord('D'),
        'KEY_E': ord('E'),
        'KEY_F': ord('F'),
        'KEY_G': ord('G'),
        'KEY_H': ord('H'),
        'KEY_I': ord('I'),
        'KEY_J': ord('J'),
        'KEY_K': ord('K'),
        'KEY_L': ord('L'),
        'KEY_M': ord('M'),
        'KEY_N': ord('N'),
        'KEY_O': ord('O'),
        'KEY_P': ord('P'),
        'KEY_Q': ord('Q'),
        'KEY_R': ord('R'),
        'KEY_S': ord('S'),
        'KEY_T': ord('T'),
        'KEY_U': ord('U'),
        'KEY_V': ord('V'),
        'KEY_W': ord('W'),
        'KEY_X': ord('X'),
        'KEY_Y': ord('Y'),
        'KEY_Z': ord('Z'),

        'KEY_a': ord('a'),
        'KEY_b': ord('b'),
        'KEY_c': ord('c'),
        'KEY_d': ord('d'),
        'KEY_e': ord('e'),
        'KEY_f': ord('f'),
        'KEY_g': ord('g'),
        'KEY_h': ord('h'),
        'KEY_i': ord('i'),
        'KEY_j': ord('j'),
        'KEY_k': ord('k'),
        'KEY_l': ord('l'),
        'KEY_m': ord('m'),
        'KEY_n': ord('n'),
        'KEY_o': ord('o'),
        'KEY_p': ord('p'),
        'KEY_q': ord('q'),
        'KEY_r': ord('r'),
        'KEY_s': ord('s'),
        'KEY_t': ord('t'),
        'KEY_u': ord('u'),
        'KEY_v': ord('v'),
        'KEY_w': ord('w'),
        'KEY_x': ord('x'),
        'KEY_y': ord('y'),
        'KEY_z': ord('z'),

        'KEY_BACKSPACE': '\x1b[D',
        'KEY_TAB': '\x1b[D',
        'KEY_CLEAR': '\x1b[D',
        'KEY_RETURN': '\x1b[D',
        'KEY_ENTER': '\x1b[D',
        'KEY_PAUSE': '\x1b[D',
        'KEY_DELETE': '\x1b[D',
        'KEY_KEYPAD_1': '\x1b[D',
        'KEY_KEYPAD_2': '\x1b[D',
        'KEY_KEYPAD_3': '\x1b[D',
        'KEY_KEYPAD_4': '\x1b[D',
        'KEY_KEYPAD_5': '\x1b[D',
        'KEY_KEYPAD_6': '\x1b[D',
        'KEY_KEYPAD_7': '\x1b[D',
        'KEY_KEYPAD_8': '\x1b[D',
        'KEY_KEYPAD_9': '\x1b[D',
        'KEY_INSERT': '\x1b[D',
        'KEY_HOME': '\x1b[D',
        'KEY_END': '\x1b[D',
        'KEY_PAGEUP': '\x1b[D',
        'KEY_PAGEDOWN': '\x1b[D',
        'KEY_F1': '\x1b[D',
        'KEY_F2': '\x1b[D',
        'KEY_F3': '\x1b[D',
        'KEY_F4': '\x1b[D',
        'KEY_F5': '\x1b[D',
        'KEY_F6': '\x1b[D',
        'KEY_F7': '\x1b[D',
        'KEY_F8': '\x1b[D',
        'KEY_F9': '\x1b[D',
        'KEY_F10': '\x1b[D',
        'KEY_F11': '\x1b[D',
        'KEY_F12': '\x1b[D',
        'KEY_F13': '\x1b[D',
        'KEY_F14': '\x1b[D',
        'KEY_F15': '\x1b[D',

        'KEY_NUMLOCK': '',
        'KEY_CAPSLOCK': '',
        'KEY_SCROLLLOCK': '',
        'KEY_RSHIFT': '',
        'KEY_LSHIFT': '',
        'KEY_RCTRL': '',
        'KEY_LCTRL': '',
        'KEY_RALT': '',
        'KEY_LALT': '',

        'KEY_RMETA': '',
        'KEY_LMETA': '',
        'KEY_RSUPER': '',
        'KEY_LSUPER': '',
        'KEY_PRINTSCR': '',
        'KEY_BREAK': '',
        'KEY_POWER': '',
        'KEY_SYSREQ': '',
    },
}

event = {}

# Create and populate dict of events (consisting of a tuple of the event,
# value, and the event_type)
for _type, _events_of_type in _events.items():
    for _event, _value in _events_of_type.items():
        event[_event] = Event(_event, _value, _type)
