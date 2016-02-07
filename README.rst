nwid
####
An experimental terminal widget (curses) manger for humans.
===========================================================
.. image: https://www.quantifiedcode.com/api/v1/project/0135ae22444d43fca231b360e6e0799c/badge.svg
  :target: https://www.quantifiedcode.com/app/project/0135ae22444d43fca231b360e6e0799c :alt: Code issues
----

Please not that this is a work in progress. Use at your own risk.

Nwid is designed to be an easy-to-use curses widget library and application
framework for building terminal GUIs with intuitive widgets, a simple and
recognizable event loop, and a container ``App`` that can be extended or used
as-is. Its design and components are somewhat inspired by the web browser DOM
and its event model. It also takes some inspiration from
`urwid <http://urwid.org/>`_ and
`npyscreen <http://npyscreen.readthedocs.org/index.html>`_.

Although there are a handful of relatively decent curses libraries, they either
are awkward to use (requiring you to do things and know things that the
framework should be doing for you) or they do too much and are difficult to
extend. The nwid philosophy is to let you manage the widgets and the framework
will do all the dirty work. The code is pythonic and easy to read, which makes
it easy to extend. Nwid is the terminal widget manager for humans.

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

