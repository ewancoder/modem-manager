Usage
=====

.. role:: i
.. role:: s

.. contents::

Starting communication
----------------------

When you first open the program, you see main window.

.. image:: Screens/MainForm.png

At start, all available ports available within OS should be updated and filled in ports list :i:`1`. You can manually refresh them after inserting new devices by clicking **"Rescan"`** :i:`2` button.

After choosing needed port, select (or input) serial port speed (baud rate) for given device :i:`3`. Check or uncheck **"Fill automatically"** :i:`4` checkbox: if it is checked, all information about modem will be filled automatically after you have connected to modem. You can also fill information manually using **"Fill information"** :i:`5` button. The same result could be achieved by using :s:`F5` key (refresh information, see :ref:`key-shortcuts`).

Click **"Open port"** :i:`6` button to start communication. If port has been successfully opened, status indicator :i:`7` will turn green. This status indicator could be 3 different colors: red for closed, green for opened, blue for *"downloading mode"*.

There's console view at the bottom of the window. Left view :i:`8` is for pretty status messages and filtered AT-command results, where right view :i:`9` is raw COM (serial) monitor which displays all that present in COM connection.

Text field :i:`10` at the bottom allows to send AT commands explicitly into modem and text field **"Search"** :i:`11` allows to search through both console windows.

.. image:: Screens/Search.png

.. note::

   Search does not work incrementally: it just highlights all found matches so you can see them distinctly.

.. _queue:

Using queue
-----------

Whether you are using console input or automatized button which processes number of tasks, these tasks will be added into the queue of commands which you can see, pause and resume. Also you can repeat last sent (unsuccessful) command.

.. image:: Screens/Queue.png

.. note::

   If you have **"Autofocus queue"** enabled in settings, this tab will be automatically opened when automatized sequence of commands is triggered (see :ref:`settings`).

Here you can see list of commands that appeared after starting modem application configuration (see :ref:`configuration`). Currently working command is highlighted by green color if it is AT-command and by blue color if it is a process which uses progressbar below (XModem uploading, analog/digital inputs configuration).

Checkbox **"Autopause"** :i:`1` makes sure that if an error occurs when command is executed, whole queue would be paused and you will be notified of that. In most cases, this checkbox should be enabled.

Button **"Pause/Resume"**  :i:`2` allows to manually pause/resume queue. If the queue is paused, you can still input new AT commands which will be immediately executed in second (parallel) queue which is always working in non-pausing mode for this case specially.

Button **"Repeat"** :i:`3` allows to repeat last (failed) AT-command if the queue is currently paused. This command is executed in second queue, so this is just an automation around typing the same command again and again.

Progressbar :i:`4` is needed for indicating progress of long events (such as downloading firmware or configuring lots of ports).

.. _settings:

ModemManager settings
---------------------

For more comfortable look and feel you may wish to setup it for your demands. To do so, go to **"Settings"** :i:`1` tab. If you wish to skip settings chapter, go to :ref:`preparation` section.

.. image:: Screens/Settings.png

In listbox **"Application language"** :i:`2` you can choose whole application language between two languages (currently): english and russian. This localizes not only user interface, but also various status messages in console view.

In listbox **"AT autocompletion"** :i:`3` you can select autocompletion type for manual AT-command input from 4 different types:

.. image:: Screens/Autocomplete.png

:i:`8` - None

:i:`9` - Suggest

:i:`10` - Append

:i:`11` - Suggest and append

.. note::

   Autocompletion uses history of used AT-commands. There's no predefined list of commands.

Checkbox **"Autofocus queue"** :i:`4` does exactly what it promises to do: it focuses **"Queue"** tab (see :ref:`queue`) when automatized queue of commands is started, so that you can see whole queue coming and going.

**"Colorize COM monitor"** :i:`5` checkbox improves look and feel of raw COM monitor at the bottom right side of application. It actually colorized input based on some rules, like orange for "quoted text".

.. image:: Screens/ColorizedCOM.png

Checkbox **"Save settings on exit"** :i:`6` is needed for saving settings and state of the application between sessions. If you want to start from current setup all the time, just uncheck this checkbox and if you change any settings, they will not remain after restart.

.. warning::

   The program will not save **"Save settings on exit"** option if it is unchecked. To explicitely save it you should use :s:`Ctrl` :s:`S` shortcut to manually save current settings (see :ref:`key-shortcuts`).

And finally, button **"Reset defaults"** :i:`7` resets all configurations to its default values without possibility to return :)

.. _preparation:

Preparation
-----------

Before start using modem, you need to prepare it for work. If you obtained clean modem without our latest application, or you wish to upgrade to the latest version and you haven't setup needed APN or other settings yet, you should do following:

.. image:: Screens/Automatic.png

:i:`1` Remap Application & Filesystem disk space (if you need it).

:i:`2` Configure external (internet) APN for your simcard.

:i:`3` Make sure needed checkboxes is checked.

:i:`4` Check these if you want to update in-modem time and then refill information from modem.

:i:`5` Finally click the **"Start"** button to get started. Then the queue (see :ref:`queue`) will be filled with needed commands and modem will proceed to setup.

If you want to update firmware (or to download it the first time), click the **"Update from cloud"** :i:`6` button. The process of updating application from the cloud is tricky though, because you will probably run into errors and will need debug skills to proceed. If you encounter any errors, please proceed to :ref:`troubleshooting` area before contacting us.

.. note::

   APN MUST be configured at least once, because the procedure of APN configuration is also PATCHING modem for correct use.

.. _configuration:

Application configuration
-------------------------

Configuring application only works if you have our application inside your modem (which is obvious).

.. image:: Screens/Configuration1.png

.. image:: Screens/Configuration2.png

:i:`1` button fills information from modem.

:i:`2` button fills information from XML config file. You can get such file with predefined settings and just load whole configuration from it.

:i:`3` button saves current on-screen configuration into XML file for future use.

:i:`4` button resets default configuration which is defined by the version of application you are using.

:i:`5` button configures all on-screen configuration into modem.

Reference manual for sections :i:`6` - :i:`13` will be added in future.

.. _troubleshooting:

Troubleshooting
---------------

Error occurs when trying updating from cloud
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If error occurred before ``at+wdss=1,1`` command is executed, it most likely happened because you have no SIM card installed. Please, check that you have SIM card installed and that your modem have reliable internet connection (correct APN is set).

Also, make sure that your modem is patched (see :ref:`preparation`). APN must be configured at least once.

Can't send command error is sometimes occurs, nothing helps unless application is restarted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is major bug with USB communication and it can occur sometimes based on Windows configuration, drivers configuration and modem configuration. This is hardware related question and low-level COM communication question, which will not be resolved in close time.

If you made your configuration in **"Configuration"** tab and then this error occured, you can just save whole configuration into XML file, restart application and load this configuration from XML file.
