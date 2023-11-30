====================================
 Installation of gtimelog for Mac OS
====================================

Purpose
=======

Run https://github.com/gtimelog/gtimelog like a native Mac OS app.

Versions
========

- Compatible with Mac OS 10.6 (Snow Leopard) to Mac OS 13.6 (Ventura)

- Currently only used and tested with Mac OS 13.6!

Prerequisites
=============

MacPorts
--------

- You need to install MacPorts from https://www.macports.org/

- To install gtk3 and the other needed components call::

      sudo port install gtk3 +quartz
      sudo port install libsecret

- To use the last released version use::

      sudo port install gtimelog

- Otherwise install it using a Git clone and ``pip install .``.

Homebrew
--------

- You need to install Homebrew from https://brew.sh/

- To install gtk3 and the other needed components call::

      brew install gtk+3
      brew install gobject-introsprection
      brew install libsoup
      brew install libsecret

- Install `gtimelog`` using a Git clone and ``pip install .``.


Installation
============

- Create a directory ``.gtimelog`` in your home directory

- Copy ``contrib/gtimelogrc.example`` to ``$HOME/.gtimelog/gtimelogrc`` and change the
  parameters as needed.

- If you are not using the ``gtimelog`` executable from
  ``/opt/local/bin/gtimelog`` you have to set the environment variable
  ``GTIMELOG_PATH`` to ``<absolute path of gtimelog directory>/bin/gtimelog``:

  - for Mavericks (10.9): see Stackoverflow_

  - for Yosemite (10.10): see Stackexchange_

  - as an example see the file ``contrib/my.gtimelog.plist``.

- To use VS Code as editor (new way, MacPorts), you

  - have to use https://github.com/gtimelog/gtimelog/pull/246

  - ``sudo port install dconf``

  - ``dconf write /org/gtimelog/editor '"open -a Visual\\\\ Studio\\\\ Code.app %s"'``
    (The four slashes are important.)

- To use VS Code as editor (new way, Homebrew), you

  - have to use https://github.com/gtimelog/gtimelog/pull/246

  - Change the default app in MacOS for text files to VS Code.

- To use VS Code as editor (old way), copy:

  - ``contrib/vscode.desktop`` to ``~/.local/share/applications``

  - ``contrib/mimeapps.list`` to ``~/.config``

  - ``contrib/gio-launch-desktop`` to ``~/bin`` (make sure it is executable)

  - *Caution:* This currently only works when gtimelog is started in an
    terminal, not when it is started as MacOS application.

.. _Stackoverflow : http://stackoverflow.com/questions/135688/setting-environment-variables-in-os-x
.. _Stackexchange : http://apple.stackexchange.com/questions/106355/setting-the-system-wide-path-environment-variable-in-mavericks

Usage
=====

- Double click on gtimelog.app in /Applications to start it.
