=====
radio
=====

**radio** is a python script to **just listen to the radio** using mplayer.

Installation
============

Run in terminal (with superuser privilegies)::

    $ pip install radio

Usage
=====

Help
----

Show some help::

    $ radio
    $ radio -h
    $ radio --help

List radios
-----------

List available radios::

    $ radio -l          # List available radios
    $ radio --list-all  # List radios and url

Play radios
-----------

Listen to the radio::

    $ radio <radio_id>

where <radio_id> must be in the radio list as shown above.
    
*Turn off* the radio by pressing "q" (as it uses mplayer).

Add/update radios
-----------------

Add/update radios (with superuser privileges)::

    $ radio --add <radio_id> <radio_name> <radio_url>

For example::

    $ radio --add madre "Radio Madre AM 530" http://200.68.81.65:8000/am530

Remove radios
-------------

Remove radios (with superuser privileges)::

    $ radio --remove <radio_id>

For example::

    $ radio --remove madre

To do
=====

- support multiples lists
- use curl/cvlc/whatever instead mplayer if available
- what more?
- help me at https://github.com/quijot/radio-package

Author
======

* Santiago Pestarini <santiagonob@gmail.com>

License
=======

radio is licensed under the *do What The Fuck you want to Public License*, WTFPL. See the LICENSE file.


