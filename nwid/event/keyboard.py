#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             keyboard.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       06/02/2017
#

"""
nwid.events.keyboard
~~~~~~~~~~~~~~~~~~~~

This module contains keyboard and signal definitions.
"""

from __future__ import absolute_import

import signal


# Note that terminal events only represent keypresses. There is no 'keyup' or 'keydown'.


KEY_A = ord('A')
KEY_B = ord('B')


SIGCONT = signal.SIGCONT
SIGWINCH = signal.SIGWINCH

KEY_ESCAPE = '\x1b'

KEY_UP = '\x1b[A'
KEY_DOWN = '\x1b[B'
KEY_RIGHT = '\x1b[C'
KEY_LEFT = '\x1b[D'

KEY_BACKSPACE = '\x1b[D'
KEY_TAB = '\x1b[D'
KEY_CLEAR = '\x1b[D'
KEY_RETURN = '\x1b[D'
KEY_ENTER = '\x1b[D'
KEY_PAUSE = '\x1b[D'
KEY_DELETE = '\x1b[D'
KEY_KEYPAD_1 = '\x1b[D'
KEY_KEYPAD_2 = '\x1b[D'
KEY_KEYPAD_3 = '\x1b[D'
KEY_KEYPAD_4 = '\x1b[D'
KEY_KEYPAD_5 = '\x1b[D'
KEY_KEYPAD_6 = '\x1b[D'
KEY_KEYPAD_7 = '\x1b[D'
KEY_KEYPAD_8 = '\x1b[D'
KEY_KEYPAD_9 = '\x1b[D'
KEY_INSERT = '\x1b[D'
KEY_HOME = '\x1b[D'
KEY_END = '\x1b[D'
KEY_PAGEUP = '\x1b[D'
KEY_PAGEDOWN = '\x1b[D'
KEY_F1 = '\x1b[D'
KEY_F2 = '\x1b[D'
KEY_F3 = '\x1b[D'
KEY_F4 = '\x1b[D'
KEY_F5 = '\x1b[D'
KEY_F6 = '\x1b[D'
KEY_F7 = '\x1b[D'
KEY_F8 = '\x1b[D'
KEY_F9 = '\x1b[D'
KEY_F10 = '\x1b[D'
KEY_F11 = '\x1b[D'
KEY_F12 = '\x1b[D'
KEY_F13 = '\x1b[D'
KEY_F14 = '\x1b[D'
KEY_F15 = '\x1b[D'

KEY_NUMLOCK = ''
KEY_CAPSLOCK = ''
KEY_SCROLLLOCK = ''
KEY_RSHIFT = ''
KEY_LSHIFT = ''
KEY_RCTRL = ''
KEY_LCTRL = ''
KEY_RALT = ''
KEY_LALT = ''

KEY_RMETA = ''
KEY_LMETA = ''
KEY_RSUPER = ''
KEY_LSUPER = ''
KEY_PRINTSCR = ''
KEY_BREAK = ''
KEY_POWER = ''
KEY_SYSREQ = ''
