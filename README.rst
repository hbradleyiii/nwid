nwid
####
A terminal widgets framework for humans.
===========================================================
.. image:: https://www.quantifiedcode.com/api/v1/project/d817599b176740e49b42d1f8402d4d3e/badge.svg
  :target: https://www.quantifiedcode.com/app/project/d817599b176740e49b42d1f8402d4d3e
  :alt: Code issues
----

Please note that this is a work in progress. The API will likely change many
times before it becomes stable. Use at your own risk.

Nwid is a terminal widgets framework for humans.

It is designed to be an easy-to-use, light-weight (no dependencies), curses
widget library and application framework for building terminal GUIs. It has
intuitive widgets, a simple and recognizable event loop, and a container
``App`` that can be extended or used as-is. Its design and components take some
inspiration from the well-known web browser DOM as well as the python packages
`urwid <http://urwid.org/>`_ and
`npyscreen <http://npyscreen.readthedocs.org/index.html>`_.

Although there already are a handful of terminal user-interface libraries in
python, I have found them to be either cumbersome to use or difficult to extend
because of their design. The python curses module is itself unweildly and
desperately needs a layer of abstraction to hide its unique details and oddly
named functions. Nwid aims to be this intuitive, easy to extend abstraction
layer. The nwid philosophy is to let you create and describe the widgets with
intuitive attributes and methods, and the framework will take care of the
cumbersome curses details. The code is pythonic and easy to read, which makes
it easy to extend.

A low-level knowledge of curses is not necessary to using this framework. To
get started, check out the examples in the examples directory. Nwid is designed
to be conceptually easy to understand, and the examples are intended to exhibit
the basic concepts in order to give a helpful overview of the capabilities and
structure of the framework. After looking at the examples, you can read
`Modules and Components`_ for more specific details about the framework.

If you have any questions, comments, or suggestions I'd love to hear them:
harold (a) bradleystudio.net


Installing and including in projects
====================================

Installing nwid
---------------

.. code:: bash

    $ git clone git@github.com:hbradleyiii/nwid.git
    $ cd <project directory>
    $ pip install -e .

Running Tests
-------------

.. code:: bash

    $ cd <project directory>
    $ py.test

Importing and Basic Usage
-------------------------

.. code:: python

    >>> import nwid

    >>> app = nwid.App()
    >>> app.run()


Modules and Components
======================

Overview
--------

The nwid framework is made of three major components, the ``App`` class for
managing windows and running the event loop, the ``Window`` class for
containing and managing widgets, and the widget module for creating the user
interactive widgets (such as, textfields, labels, and dropdown boxes).

The ``App`` is the base controller for the application. Besides controling the
event loop, it is responsible for initializing the curses environment and
handling the screen object. This class can be used as-is or may be extended by
a custom class with application-specific controller methods. The ``App`` class
has a special property, the ``App.window_stack``, that keeps track of the
current window and any open window that has not yet been closed but is covered
up (partly or completely) by the current window.

For instance, the first window may be a form that has a button that opens a
second window with a select box containing a list of options to choose from.
The first window hasn't yet closed but is waiting for the second window to
provide the user selected choice. At this point, the second window is the
second and top-most window on the stack. Any events that are triggered are now
given to this window. It may completely cover the first window or might only
cover a portion of it being centered on the screen with the edges revealing the
first window behind it. This second window may contain a select box with a list
of several objects or strings to pass back to the first window. One of these
options might be 'new', indicating that the user wishes to create a new string
or object. Selecting this item, might open a third window for this task,
putting this third window on top of the stack. This stacking could go on
indefinitely with each window appending to the ``App.window_stack``. When the
topmost window is closed, this window is 'popped' from the stack and the next
window down in the stack is given back the focus. When an ``App`` no longer has
any windows, the application is closed.

The ``Window`` class is the container class for the widgets. It sets the bounds
for where a widget can be drawn. It may have a border and title set. Note that
this is not the same thing as the curses window object. Although it should have
a reference to this object in ``Window.screen``.

A widget is a user interface object that can be displayed in a window. It is
defined by its height and width, its location on the window, and its foreground
and background colors. It has contents such as a string of text or a more
complicated widget may contain other widgets. In fact, a ``Window`` class is
actually a special kind of top-level widget. You can create your own custom
widgets by extending ``widget.Base``, although nwid comes with a number of
useful generic widgets such as ``TextBox``, ``LabledTextBox``, ``CheckBox``,
``String``, ``Button``, ``Label``, and ``SelectBox``. Widgets can register
events to callback functions in order to handle keyboard or mouse events.
