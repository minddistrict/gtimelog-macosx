=======================================
 Installation of gtimelog for Mac OS X
=======================================

Versions
========

- Compatible with Mac OS 10.6 (Snow Leopard) to Mac OS 10.14 (Mojave)

- Currently only used and tested with Mac OS 12.3!

Prerequisites
=============

- You need to install MacPorts from http://www.macports.org/

- You are able to install gtimelog in three variants:

    - gtimelog3 (gtk3)
    - Quartz (native Mac OS UI)
    - X11

The variants are listed from most preferred to least.

Prerequisites for the gtimelog3 variant
---------------------------------------

To install gtk3 and the other needed components for gtimelog3 call::

      sudo port install libsoup
      sudo port install libsecret
      sudo port install adwaita-icon-theme
      sudo port install pango +no_x11+quartz
      sudo port install gtk3 +quartz
      ...


Prerequisites for the Quartz variant
------------------------------------

To install gtk+ and the other needed components for Quartz call::

      sudo port install glib2 +quartz
      sudo port install cairo +no_x11+quartz
      sudo port install pango +no_x11+quartz
      sudo port install gtk2 +no_x11+quartz
      sudo port install py27-lxml
      sudo port install py27-cairo -x11
      sudo port install py27-pygtk +quartz
      sudo port install py27-virtualenv

Prerequisites for the X11 variant
---------------------------------

Install XQuartz (https://www.xquartz.org).

To install gtk+ and the other needed components for X11 call::

      sudo port install cairo +x11
      sudo port install pango +x11
      sudo port install gtk2 +x11
      sudo port install glib2 +x11
      sudo port install py27-lxml
      sudo port install py27-cairo +x11
      sudo port install py27-pygtk +x11
      sudo port install py27-virtualenv
      sudo port install curl-ca-bundle

Switch between X11 and Quartz variant
-------------------------------------

- To switch between X11 and Quartz you have to install gtk+ for the new variant (see above).

- Uninstall the previous variant::

   sudo port uninstall inactive

- Then you have to uninstall the python bindings and a variant  dependent library::

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

- Create a virtualenv for the python installed above with all installed
  libraries::

    /opt/local/bin/virtualenv-2.7 --system-site-packages gtimelog
    cd gtimelog
    bin/pip install zc.buildout

- To use a released version get the latest release of ``gocept.gtimelog`` from
   http://download.gocept.com/packages, extract it and change into the newly
   created directory.

- To use a source checkout clone the repository from
   https://github.com/gocept/gocept.gtimelog.git and change into the directory
   of the checkout.

- Install the dependencies::

    ../bin/buildout

- Set the environment variable ``GTIMELOG_PATH`` to
  ``<absolute path of gtimelog directory>/bin/gtimelog``.

  - for Mavericks (10.9): see Stackoverflow_

  - for Yosemite (10.10): see Stackexchange_

  - as an example see the file ``my.gtimelog.plist`` right beside this README.

- Create an application shortcut

    mkdir -p /Applications/gtimelog.app/Contents/MacOS
    ln -s  <Path to gtimelog virtualenv>/bin/gtimelog /Applications/gtimelog.app/Contents/MacOS/gtimelog

.. _Stackoverflow : http://stackoverflow.com/questions/135688/setting-environment-variables-in-os-x
.. _Stackexchange : http://apple.stackexchange.com/questions/106355/setting-the-system-wide-path-environment-variable-in-mavericks

Usage
=====

- Double click on gtimelog.app in /Applications to start it.

Update released version installation
====================================

Get the new version from http://download.gocept.com/packages an install it as described above. Than restart gtimelog.app.

Update source checkout
======================

Go to directory where you checked out ``gocept.gtimelog`` and then call::

    hg pull -u
    bin/buildout
