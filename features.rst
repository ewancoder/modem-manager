Features
========

.. role:: s

Functionality
-------------

* Stable response from modem

  .. image:: Figures/Stable.png

* Query all information about embedded module

  .. image:: Figures/Information.png

  + General information
  + Memory sizes
  + Firmware information

* Queue of commands

  .. image:: Figures/Queue.png

  + All commands added to one queue executed in the background thread
  + User can pause and resume commands, added to the queue
  + Queue can be automatically stopped when an error occur (if configured)
  + There is a list of current commands in the queue. Currently running command is highlighted
  + When started automatic modem configuration, queue tab can be automatically selected (if not disabled)

* Uploading firmware, using XModem protocol

  .. image:: Figures/XModem.png

* Automatic modem configuration

  .. image:: Figures/Automate.png

  + Erase application
  + Write bootloader and firmware
  + Remap memory

    - Choose both AD and FS sizes, then let automatic mapper do the work for you
    - Minimal size of AD aread is 256 KiB (for safety)
    - Visual view of mapped areas

  + Write application
  + Prepare modem for remote firmware writing
  + Sync time

Usability
---------

* Command autocompletion and suggestion based on input history

  .. image:: Figures/Autocompletion.png

* Localization of every UI element as well as status messages

  .. image:: Figures/Localization.png

* Remember all configured settings per sessions

  .. image:: Figures/Settings.png

Visuals
-------

.. image:: Figures/Overall.png

* Clean and filtered **Console window**

  .. image:: Figures/Console.png

  + Command timespan
  + Colorful statuses in console

* Raw serial **Monitor window**

  .. image:: Figures/Monitor.png

  + Keep all history until another port is used

* Search through both console windows

  .. image:: Figures/Search.png

* Colorful and noticeable status boxes

  .. image:: Figures/States.png

* Flexible layout - windows are totally resizeable to any screen resolution, in-form splits are totally movable whenever you want. Also, you can show/hide information/console view (F11/F12)

  .. image:: Figures/Resizeable.png
     :width: 30em

* Progressbar shows file uploading

  .. image:: Figures/Uploading.png

.. _key-shortcuts:

Keyboard shortcuts
------------------

Global:

:s:`F1` - PDF documentation will be opened if present, otherwise the website will be shown

:s:`Ctrl` + :s:`F1` - Show Machine ID: needed for license check (full version unlock)

:s:`F5` - Update (fill) modem information

:s:`F6` - Update (fill) modem configuration

:s:`F9` - Store current modem in XML database of installed modems

:s:`F11` - Hide / show **Console** view

:s:`F12` - Hide / show **Main** view

:s:`Ctrl` + :s:`L` - Clear console

:s:`Ctrl` + :s:`S` - Save all settings, includes current APN configuration

:s:`Ctrl` + :s:`M` - RAW console mode (full screen COM monitor), could be used with Detach mode (right click -> Detach)

:s:`Ctrl` + :s:`Space` - Pause/Resume queue

Command input field:

:s:`Return` - Send command

:s:`Ctrl` + :s:`Z` - Send data in download mode (substitute character at the end)

Window focus:

:s:`Ctrl` + :s:`I` - Focus AT command input field

:s:`Ctrl` + :s:`F` - Focus search field

:s:`Alt` + :s:`1` - switch to 1st **Connection** tab

:s:`Alt` + :s:`2` - switch to 2nd **Queue** tab

:s:`Alt` + :s:`3` - switch to 3rd **Settings** tab

:s:`Alt` + :s:`4` - switch to 4th **Information** tab

:s:`Alt` + :s:`5` - switch to 5th **Automatic** tab

:s:`Alt` + :s:`6` - switch to 6th **Configuration** tab

.. note::

   For switching tabs you can use :s:`Ctrl` as well.

Development
-----------

.. image:: Figures/Development.png

* Clean code base and architecture
* Minimal dependencies
* Threading: all the work done in the background thread, UI does not freeze
* Separate classes do separate work
* Constructive comments for most code blocks
* Code enclosed in #regions for clarity
