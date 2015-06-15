Использование
=============

.. role:: i
.. role:: s

.. contents:: Содержание

Установка соединения
--------------------

Когда Вы первый раз откроете программу, Вы увидите следующее окно.

.. image:: ../Screens/MainForm-ru.png

При запуске, все доступные в системе порты обновляются и добавляются в список портов :i:`1`. Вы можете вручную обновить список доступных портов, после добавления новых устройств, нажатием кнопки **"Открыть порт"** :i:`2`.

После выбора необходимого порта, выберите (или введите) необходимую скорость передачи данных (baud rate) для выбранного устройства :i:`3`. Установите флажок **"Заполнить автоматически"** :i:`4` если Вы хотите чтобы программа заполнила информацию о модеме автоматически при подключении к устройству. Также в любой момент можно сделать это вручную используя кнопку **"Заполнить информацию"** :i:`5`. Тот же результат может быть получен нажатием горячей клавиши :s:`F5` (обновить информацию, см. :ref:`key-shortcuts`).

Для подключения к модему нажмите кнопку **"Открыть порт"** :i:`6`. Если порт был успешно открыт, индикатор текущего статуса :i:`7` станет зелёным. Индикатор статуса может быть трех разных цветов: красный при закрытом порту, зелёный - при открытом, синий - в режиме *"загрузки"*.

В нижней части окна располагается консольный монитор. Левая :i:`8` часть отвечает за красивые статусные сообщения и фильтрованный вывод AT-команд, правая :i:`9` часть является монитором последовательного COM-соединения и отображает всё что попадает в COM-порт.

Текстовое поле :i:`10` в самом низу позволяет слать AT-команды модему напрямую. Текстовое поле :i:`11` осуществляет поиск по обоим консольным окнам.

.. image:: ../Screens/Search.png

.. note::

   Поиск работает не инкрементально: он лишь подсвечивает все совпадения для удобного просмотра результатов.

.. _queue:

Очередь команд
--------------

При общении с модемом, будь то ручные команды или автоматическая кнопка настройки модема, AT-команды складываются в *"очередь"* команд. Очередь можно приостанавливать и возобнавлять, а также повторять последнюю (неудавшуюся) команду.

.. image:: ../Screens/Queue-ru.png

.. note::

   Если флажок **"Автоматически показывать очередь"** (в настройках) включен, вкладка очереди будет автоматически открыта когда автоматизированный набор команд будет запущен на исполнение (см. :ref:`settings`).

На скриншоте отображён список команд, появившихся после запуска конфигурирования приложения модема (см. :ref:`configuration`). Текущая работающая команда подсвечена зелёным цветом если это AT-команда, и синим цветом если это длительный процесс (загрузка прошивки по протоколу XModem, перенастройка аналоговых и цифровых входов).

Флажок **"Автопауза"** :i:`1` отвечает за приостановку очереди в случае возникновения ошибок при выполнении команды. В большинстве сценариев, этот влажок должен быть активен.

Кнопка **"Пауза/Продолжить"** :i:`2` позволяет вручную приостановить/возобновить очередь. Если очередь приостановлена, Вы всё ещё можете посылать модему AT-команды, которые будут выполнены сразу же после ввода в параллельной (другой) очереди, работающей без остановок специально для этого применения.

Кнопка **"Повторить"** :i:`3` позволяет повторить последнюю (неудавшуюся) AT-команду если очередь в данный момент приостановлена. Эта команда исполняется в параллельной очереди, позволяя заменить ввод одной и той же команды вручную.

Индикатор состояния :i:`4` нужен для отображения прогресса долгих событий (таких как загрузка прошивки или перенастройка большого количества портов).

.. _settings:

Настройки ModemManager
----------------------

Для более комфортной работы с программой Вы можете настроить её удовлетворяющим Вас образом. Для этого перейдите на вкладку **"Настройки"** :i:`1`. Если Вы желаете пропустить часть по настройке программы, можете перейти к части :ref:`preparation`.

.. image:: ../Screens/Settings-ru.png

In listbox **"Application language"** :i:`2` you can choose whole application language between two languages (currently): english and russian. This localizes not only user interface, but also various status messages in console view.

In listbox **"AT autocompletion"** :i:`3` you can select autocompletion type for manual AT-command input from 4 different types:

.. image:: ../Screens/Autocomplete.png

:i:`8` - None

:i:`9` - Suggest

:i:`10` - Append

:i:`11` - Suggest and append

.. note::

   Autocompletion uses history of used AT-commands. There's no predefined list of commands.

Checkbox **"Autofocus queue"** :i:`4` does exactly what it promises to do: it focuses **"Queue"** tab (see :ref:`queue`) when automatized queue of commands is started, so that you can see whole queue coming and going.

**"Colorize COM monitor"** :i:`5` checkbox improves look and feel of raw COM monitor at the bottom right side of application. It actually colorized input based on some rules, like orange for "quoted text".

.. image:: ../Screens/ColorizedCOM.png

Checkbox **"Save settings on exit"** :i:`6` is needed for saving settings and state of the application between sessions. If you want to start from current setup all the time, just uncheck this checkbox and if you change any settings, they will not remain after restart.

.. warning::

   The program will not save **"Save settings on exit"** option if it is unchecked. To explicitely save it you should use :s:`Ctrl` :s:`S` shortcut to manually save current settings (see :ref:`key-shortcuts`).

And finally, button **"Reset defaults"** :i:`7` resets all configurations to its default values without possibility to return :)

.. _preparation:

Preparation
-----------

Before start using modem, you need to prepare it for work. If you obtained clean modem without our latest application, or you wish to upgrade to the latest version and you haven't setup needed APN or other settings yet, you should do following:

.. image:: ../Screens/Automatic.png

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

.. image:: ../Screens/Configuration1.png

.. image:: ../Screens/Configuration2.png

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