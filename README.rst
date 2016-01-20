=====
radio
=====

**radio** is a python script to **just listen to the radio** [*]_.

.. [*] Requires **mplayer**, **ffplayer** (ffmpeg package) or **cvlc** (vlc package). Priority or alternative players yet to make *customizable* in future versions.

Installation
============

Run in terminal (with superuser privilegies)::

    $ pip install radio

Usage
=====

Help
----

Show some help::

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
    
*Turn off* the radio by pressing "q" (if using mplayer) or with Ctrl-<C> (if using ffplay or cvlc).

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

    $ radio --remove mitre

Version
-------

Show version::

    $ radio -v
    $ radio --version

To do
=====

- support multiples lists
- support searching / filtering lists (something like *radio -s Rosario* to search radios from Rosario)
- customize player and priorities or autodetect (something like *rifle* in the *ranger* package)
- what more?
- help me at https://github.com/quijot/radio-package

Author
======

* `quijoT <https://github.com/quijoti>`_ (Santiago Pestarini <santiagonob@gmail.com>)

Collaborators
-------------

* `sdeancos <https://github.com/sdeancos>`_ (Samuel de Ancos)

License
=======

radio is licensed under the *do What The Fuck you want to Public License*, WTFPL. See the LICENSE file.

