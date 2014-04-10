=====
radio
=====

**radio** is a python script to just listen to the radio using mplayer.

Installation
============

Run in terminal::

    $ sudo pip install radio

Usage
=====

List available radios::

    $ radio -l

Listen to the radio::

    $ radio <radio_id>

where <radio_id> must be in the radio list as shown above
    
Turn off the radio by pressing "q" (as it uses mplayer).

Add/update radios (with superuser privileges)::

    $ radio -a <radio_id> <radio_name> <radio_url>

For example::

    $ radio -a madre "Radio Madre AM 530" http://200.68.81.65:8000/am530

Delete radios (with superuser privileges)::

    $ radio -d <radio_id>

To do
=====

- support multiples lists
- use curl instead mplayer if available
- use cvlc instead mplayer if available
- what more?
- help me at https://github.com/quijot/radio-package

Author
======

* Santiago Pestarini <santiagonob@gmail.com>

License
=======

radio is licensed under the *do What The Fuck you want to Public License*, WTFPL. See the LICENSE file.

