#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             test_sgr.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       06/16/2017
#

"""
Unittests for nwid.terminal.terminal_string module.
"""

from __future__ import absolute_import

from nwid.terminal import codes as code
from nwid.terminal import colors as color
from nwid.terminal import sgr, TerminalString
from nwid.terminal.terminal_string import EscapeMarker


## Test TerminalString object ##

def test_TerminalString_has_a_string_attribute():
    """A TerminalString object has a string attribute."""
    terminal_string = TerminalString('This is a string.')
    assert terminal_string.string == 'This is a string.'

def test_TerminalString_string_attribute_can_contain_escape_sequence():
    """A TerminalString object's string attribute can contain an escape
    sequence."""
    string = color.bg_red('This is a string.')
    expected = sgr.create(code.BG_RED) + 'This is a string.' + sgr.reset()
    terminal_string = TerminalString(string)
    assert terminal_string.string == expected

    string = color.bg_white(color.red('This ') + color.green('is ') + color.underline('a ') + 'string.')
    expected = sgr.create(code.BG_WHITE) + \
            sgr.create(code.RED) + 'This ' + sgr.reset() + \
            sgr.create(code.BG_WHITE) + \
            sgr.create(code.GREEN) + 'is ' + sgr.reset() + \
            sgr.create(code.BG_WHITE) + \
            sgr.create(code.UNDERLINE) + 'a ' + sgr.reset() + \
            sgr.create(code.BG_WHITE) + \
            'string.' + sgr.reset()
    terminal_string = TerminalString(string)
    assert terminal_string.string == expected

def test_TerminalString_gives_its_string_attribute_when_cast_as_a_string():
    """A TerminalString object can be cast to a string."""
    terminal_string = TerminalString('This is a string.')
    assert str(terminal_string) == 'This is a string.'
    assert terminal_string.__str__() == 'This is a string.'

def test_TerminalString_parses_and_marks_its_string_for_non_printable_chars():
    """A TerminalString parses its string and marks non-printable
    characters."""
    terminal_string = TerminalString(color.red('This is a string.'))
    expected = [
        EscapeMarker(0, 4),
        EscapeMarker(22, 25),
    ]
    assert terminal_string.escape_markers == expected
    assert terminal_string.string[5:22] == 'This is a string.'

    terminal_string = TerminalString('\bThis is a string.\a')
    expected = [
        EscapeMarker(0, 0),
        EscapeMarker(18, 18),
    ]
    assert terminal_string.escape_markers == expected
    assert terminal_string.string[1:18] == 'This is a string.'

    terminal_string = TerminalString(
        color.red(
            'This ' + 
            color.bold('is ') + 
            color.bg_white('a ') + 
            'string.', color.bg_black
        )
    )
    expected = [
        EscapeMarker(0, 7),
        EscapeMarker(13, 16),
        EscapeMarker(20, 23),
        EscapeMarker(24, 31),
        EscapeMarker(32, 36),
        EscapeMarker(39, 42),
        EscapeMarker(43, 50),
        EscapeMarker(58, 61)
    ]
    just_the_string = terminal_string.string[8:13] + \
        terminal_string.string[17:20] + \
        terminal_string.string[37:39] + \
        terminal_string.string[51:58]
    assert terminal_string.escape_markers == expected
    assert just_the_string == 'This is a string.'

def test_TerminalString_has_a_len_method():
    """A TerminalString has a len method."""
    terminal_string = TerminalString('This is a string.')
    assert len(terminal_string) == 17

def test_TerminalString_len_method_ignores_escape_sequences():
    """A TerminalString's len method ignores escape sequences."""
    terminal_string = TerminalString(color.red('This is a string.'))
    assert len(terminal_string) == 17

    terminal_string = TerminalString(
        color.red(
            'This ' + 
            color.bold('is ') + 
            color.bg_white('a ') + 
            'string.', color.bg_black
        )
    )
    assert len(terminal_string) == 17

def test_TerminalString_indexing_ignores_escape_sequences():
    """Indexing a TerminalString ignores escape sequences."""
    string = 'This is a string.'
    terminal_string = TerminalString(string)

    assert string[0]  == terminal_string[0]
    assert string[1]  == terminal_string[1]
    assert string[2]  == terminal_string[2]
    assert string[4]  == terminal_string[4]
    assert string[8]  == terminal_string[8]
    assert string[16] == terminal_string[16]

    string = 'This is a string.'
    terminal_string = TerminalString(
        color.red(
            'This ' + 
            color.bold('is ') + 
            color.bg_white('a ') + 
            'string.', color.bg_black
        )
    )

    assert string[0]  == terminal_string[0]
    assert string[1]  == terminal_string[1]
    assert string[2]  == terminal_string[2]
    assert string[4]  == terminal_string[4]
    assert string[8]  == terminal_string[8]
    assert string[16] == terminal_string[16]

def test_TerminalString_splicing_ignores_escape_sequences_for_positioning_but_includes_them():
    """Splicing a TerminalString ignores escape sequences for positioning but
    includes them in the returned string."""
    string = 'This is a string.'
    terminal_string = TerminalString(string)

    assert string[:5]  == terminal_string[:5]
    assert string[1:4]  == terminal_string[1:4]
    assert string[6:11]  == terminal_string[6:11]
    assert string[8:16] == terminal_string[8:16]

    string = 'This is a string.'
    terminal_string = TerminalString(
        color.red(
            'This ' + 
            color.bold('is ') + 
            color.bg_white('a ') + 
            'string.', color.bg_black
        )
    )
    assert terminal_string[0:5] == sgr.create(code.RED, code.BG_BLACK) + 'This ' + sgr.reset()
    assert terminal_string[1:4] == sgr.create(code.RED, code.BG_BLACK) + 'his' + sgr.reset()
    assert terminal_string[6:11] == sgr.create(code.RED, code.BG_BLACK) + \
            sgr.create(code.BOLD) + 's ' + sgr.reset() + \
            sgr.create(code.RED, code.BG_BLACK) + \
            sgr.create(code.BG_WHITE) + 'a ' + sgr.reset() + \
            sgr.create(code.RED, code.BG_BLACK) + \
            's' + sgr.reset()

    assert terminal_string[9:17] == sgr.create(code.RED, code.BG_BLACK) + \
            sgr.create(code.BOLD) + sgr.reset() + \
            sgr.create(code.RED, code.BG_BLACK) + \
            sgr.create(code.BG_WHITE) + ' ' + sgr.reset() + \
            sgr.create(code.RED, code.BG_BLACK) + \
            'string.' + sgr.reset()

def test_TerminalString_splicing_works_with_negative_values():
    """Splicing a TerminalString works with negative values."""
    string = 'This is a string.'
    terminal_string = TerminalString(string)

    assert string[:-12]  == terminal_string[:-12]
    assert string[-16:4]  == terminal_string[-16:4]
    assert string[-11:-6]  == terminal_string[-11:-6]
    assert string[-8:-1] == terminal_string[-8:-1]

    string = 'This is a string.'
    terminal_string = TerminalString(
        color.red(
            'This ' + 
            color.bold('is ') + 
            color.bg_white('a ') + 
            'string.', color.bg_black
        )
    )
    assert terminal_string[:-12] == sgr.create(code.RED, code.BG_BLACK) + 'This ' + sgr.reset()
    assert terminal_string[-16:4] == sgr.create(code.RED, code.BG_BLACK) + 'his' + sgr.reset()
    assert terminal_string[-11:-6] == sgr.create(code.RED, code.BG_BLACK) + \
            sgr.create(code.BOLD) + 's ' + sgr.reset() + \
            sgr.create(code.RED, code.BG_BLACK) + \
            sgr.create(code.BG_WHITE) + 'a ' + sgr.reset() + \
            sgr.create(code.RED, code.BG_BLACK) + \
            's' + sgr.reset()

    assert terminal_string[-8:-1] == sgr.create(code.RED, code.BG_BLACK) + \
            sgr.create(code.BOLD) + sgr.reset() + \
            sgr.create(code.RED, code.BG_BLACK) + \
            sgr.create(code.BG_WHITE) + ' ' + sgr.reset() + \
            sgr.create(code.RED, code.BG_BLACK) + \
            'string' + sgr.reset()

def test_TerminalString_splicing_works_with_step_value():
    """Splicing a TerminalString works with step value."""
    # TODO: Not yet implemented.
    pass
