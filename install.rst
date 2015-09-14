Installation
------------

.. note::

    This program is portable and does not need installation. However, if you want offline documentation and/or localization files, you should install and use the program from the folder with all corresponding files. Also, you may need to install Sierra Wireless USB driver, which is packed inside the installation.

1. Choose preferred installation language. This language will only be used for the installation: you can switch interface languages inside the program later. Note that if your OS does not have preferred language installed, you will not be able to choose this language.

   Currently (release |release|), only english and russian languages are supported both in Modem Manager and in its documentation. Although, translation can be made quickly and effortlessly from the technical point of view.

.. todo::

    Maybe write here "You can also contribute" if our politics allows users to contribute translations. Then also add latest translation files (or at least translation format) to the "Contributing" page (create it as well).

.. todo::

    Remove "only english and russian" notice after more languages will be supported.

2. Accept license agreement.

   Currently (release |release|), we are working on license agreement, so there's just copyright notice. This means you agree that the rights to the software are owned by us. Later, when license agreement will be officially added, you'll need to agree to it to continue using the program.

.. todo::

   Remove note about missing license.

3. Choose folder where Modem Manager will be installed. Modem Manager installs some additional files like localization and help files.

.. warning::

   Note that if your OS does not allow write access to the folder where Modem Manager will be installed, the program will not create log files when in use. Also, it may not create some other files, so please make sure that your user does have correct rights.

   In Windows 10 Program Files folder access is denied to regular user by default, so you'd have to start the program with Administrator rights.

   This should be fixed in later versions of the program, where log files will be stored in Documents (or temporary) folder.

.. todo::

   Fix filesystem access rights and remove the warning above.

4. Choose which files to install. You have 3 options:

    1. Full installation. All files will be installed, including documentation, localization and drivers.
    2. Compact (minimal) installation. Only core files will be installed: the executable itself and the copyright notice (license agreement).
    3. Custom installation. You can choose which files to install. This option will be selected automatically if you check/uncheck items manually.

5. Choose program shortcut to be created in the Start Menu folder. If you don't want it to be created, you can check "Don't create a Start Menu folder".

6. Check "Install Sierra Wireless USB drivers" checkbox to install USB driver. The driver is needed to communicate with modem over miniUSB cable. If you already have it installed, you can uncheck it. Uncheck "Create a desktop icon" if you don't want it to be created.

.. note::

    "Install Sierra Wireless USB drivers" checkbox will only appear if you have selected it in installed files selection list before.

7. Make sure that everything suits your needs and click Install button to begin the installation.

8. Finally uncheck "Launch Technikon Modem Manager" if you don't want it to launch right away and finish the installation.
