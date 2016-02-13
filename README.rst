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

