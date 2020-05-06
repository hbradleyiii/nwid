#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             hello_world.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       02/07/2016
#

from __future__ import absolute_import

import nwid

class HelloWorldWindow(nwid.Window):
    """An nwid Hello World Window Widget."""

    # This describes the attributes of the main window of the HelloWorldWindow.
    attributes = {
        'border' : True,
        'scrollable' : False,
        'align' : nwid.ALIGN_LEFT,
        'width' : nwid.MAX_WIDTH,
        'height' : nwid.MAX_HEIGHT,
        'callback' : self.say_hello,
        'title' : 'An nwid Hello World Application!',
        'children' : {
            nwid.LabeledTextBox : {
                'name' : 'name',
                'text' : 'Your name:',
                'validator' : self.validate_name,
            },
            nwid.Button : {
                'text' : 'Click me!',
                'click' : self.submit,
            }
        }
    }

    def validate_name(self):
        """A simple validator function for a TextBox."""
        if self.name != '':
            return True
        return False

    def submit(self):
        """The callback function for the submit button."""
        if self.name.validate():
            self.name = self.window.children
            raise CloseRunCallback(self.name)

    def say_hello(self, name):
        """The callback function that is run after closing the window."""
        print name


hello_world = nwid.App()
hellow_world.current_window = HelloWorldWindow()
hello_world.run()
