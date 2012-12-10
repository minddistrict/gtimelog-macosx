=======================================
 Installation of gtimelog for Mac OS X
=======================================

Versions
========

- Compatible with:

  - Mac OS 10.6 (Snow Leopard)

  - Mac OS 10.7 (Lion)


Prerequisites
=============

- You need to install MacPorts from http://www.macports.org/

- You are able to install gtimelog for Quartz (native Mac OS UI) or X11
  where the former should be preferred because of the better integration in
  the OS.

- gtimelog needs gtk+.

  - To install gtk+ for Quartz call::

    sudo port install cairo +no_x11+quartz
    sudo port install pango +no_x11+quartz
    sudo port install gtk2 +no_x11+quartz

  - To install it for X11 call::

    sudo port install cairo +x11
    sudo port install pango +x11
    sudo port install gtk2 +x11

- gtimelog needs some other components, install them (for Quartz) using::

     sudo port install py27-lxml
     sudo port install py27-cairo -x11
     sudo port install py27-gtk +quartz

  resp. (for X11)::

     sudo port install py27-lxml
     sudo port install py27-cairo +x11
     sudo port install py27-gtk +x11


Switch between X11 and Quartz variant
-------------------------------------

- To switch between X11 and Quartz you have to install gtk+ for the
  new variant (see above).

- Uninstall the previous variant::

  sudo port uninstall inactive

- Then you have to uninstall the python bindings and a variant
  dependent library::

  sudo port uninstall py27-gtk py27-cairo libglade2

- And reinstall them (Quartz)::

    sudo port install py27-cairo -x11
    sudo port install py27-gtk +quartz

  resp. (X11)::

    sudo port install py27-cairo +x11
    sudo port install py27-gtk +x11

- Then you can restart gtimelog which than runs using the new UI variant.


Installation
============

- Create a directory .gtimelog in your home directory

- Copy orig/gtimelogrc.example to $HOME/.gtimelog/gtimelogrc and change the
  paramaters as needed. (See also orig/README.txt)

- Install the gocept.gtimelog egg:

  - python 2.7:

    sudo /opt/local/bin/easy_install-2.7 -f http://download.gocept.com/packages gocept.gtimelog

When using another Python (e. g. virtualenv) you need to edit the runner in
"gtimelog.app/Contents/MacOS/gtimelog" to point to your Python.

Usage
=====

- Double click on gtimelog.app to start it.

Update
======

- Update the gocept.gtimelog egg:

  - python 2.7:

    sudo /opt/local/bin/easy_install-2.7 -U -f http://download.gocept.com/packages gocept.gtimelog

- Restart gtimelog.app.
