#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             app.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/06/2016
#

from __future__ import absolute_import

import curses
import nwid

app = nwid.App()

app.window.add( {
    nwid.Title : { 'text' : 'An nwid App!' },
    nwid.LabeledTextBox : {
        'text' : 'Your input:',
        'validator' : App.validate_function,
        'name' : '',
    },
    nwid.Button : {
        'text' : 'Click me!',
        'click' : App.callback_function,
    },
})

app.run()
