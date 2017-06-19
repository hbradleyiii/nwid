#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             terminal_string.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       05/28/2017
#

"""
nwid.terminal.terminal_string
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TODO: Write logic in TerminalString to recognize other kinds of escape
sequences.

@see: https://en.wikipedia.org/wiki/ANSI_escape_code
      http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-048.pdf
"""

from __future__ import absolute_import

from collections import namedtuple
from nwid.terminal import sgr
import string


EscapeMarker = namedtuple('EscapeMarker', ['start', 'stop'])


class TerminalString(object):
    """A TerminalString is a special string that can contain CSI escape
    sequences for terminal attributes such as color and bold.

    These escape sequences are ignored for functions like len() and are handled
    intelligently when splicing the string."""

    def __init__(self, string=''):
        self.set(string)

    def __repr__(self):
        return 'TODO'

    def __str__(self):
        return self.string

    def set(self, string):
        self.string = string
        self.parse_escape_markers()

    def parse_escape_markers(self):
        """Parses self.string for any CSI escape sequences or other
        non-printable characters."""
        sequence_start = None
        self.escape_markers = []
        for index, char in enumerate(self.string):
            # Mark the stop of an escape sequence
            if sequence_start is None and char in string.letters:
                self.escape_markers.append(EscapeMarker(sequence_start, index))
                sequence_start = None  # Reset start sequence 

            # Mark the beginning of an escape sequence
            elif char == '\033' and self.string[index+1] == '[':
                sequence_start = index

            # Mark other non-printable characters
            elif char not in string.printable:
                self.escape_markers.append(EscapeMarker(index, index))

    def __len__(self):
        length = len(self.string)
        for escape_marker in self.escape_markers:
            length = length - (escape_marker.stop - escape_marker.start + 1)
        return length

    def __add__(self, other):
        try:
            return TerminalString(self.string + other.string)
        except AttributeError:
            return TerminalString(self.string + other)

    def __radd__(self, other):
        try:
            return TerminalString(other.string + self.string)
        except AttributeError:
            return TerminalString(other + self.string)

    def upper(self):
        return TerminalString(self.string.upper())

    def lower(self):
        return TerminalString(self.string.lower())

    def count(self, *args):
        return TerminalString(self.string.count(*args))

    def find(self, *args):
        return TerminalString(self.string.find(*args))

    def replace(self, *args):
        return TerminalString(self.string.replace(*args))

    def format(self, *args, **kwargs):
        return TerminalString(self.string.format(*args, **kwargs))

    def vformat(self, *args, **kwargs):
        return TerminalString(self.string.vformat(*args, **kwargs))

    def __getitem__(self, key):
        """Retrieves the string based on an index or a slice.
        Ignores the escape sequences, but returns them in a slice."""
        try:  
            string = ''
            reset = ''

            start = key.start
            stop = key.stop

            print(stop)

            for marker in self.escape_markers:
                # Stop when there are no markers before key.stop
                if stop <= marker.start: break

                # Increment the key.start for every escape sequence before it
                # and add these to the front of the string we will return.
                if start > marker.start:
                    start = start + (marker.stop - marker.start + 1)
                    string = string + self.string[marker.start:marker.stop+1]

                # Increment the key.stop for every escape sequence before it
                stop = stop + (marker.stop - marker.start + 1)

            # Add all escape sequences prior to splice and the splice (including
            # sequences inside the splice).
            string = string + self.string[slice(start, stop)]

            # Add a reset at the end if there are escapes in this string
            if self.escape_markers != []:
                string = string + sgr.reset()

            return string

        except AttributeError:
            for marker in self.escape_markers:
                if key < marker.start: break
                key = key + (marker.stop - marker.start + 1)

            return self.string[key]

    def __getslice__(self, i, j):
        return self.__getitem__(slice(i, j))
