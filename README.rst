=====
radio
=====

**radio** is a command line tool to **just listen to the radio**.

Installation
============

    ``pip install radio``

Usage
=====

    ``radio [OPTIONS] COMMAND [ARGS]...``

Options:

  --version  Show the version and exit.
  --help     Show this message and exit.

Commands
--------

  add     Add or update a radio information.
  play    Play a radio.
  remove  Remove a radio information.
  search  Search radio in the available radios.
  show    Show all radios information.

add
^^^

Add or update a radio information.

Usage:
    ``radio add [OPTIONS] RADIO_ID``

Options:
  -n, --name TEXT  Radio complete fancy name.  [required]
  -u, --url TEXT   Radio playable streaming url.  [required]
  --help           Show this message and exit.

For example::

    radio add convos --name "Radio Con Vos FM 89.9" --url https://server1.stweb.tv/rcvos/live/chunks.m3u8

play
^^^^

Play a radio.

Usage:
    ``radio play [OPTIONS] RADIO_ID``

Options:
  --help  Show this message and exit.
    
*Turn off* the radio by pressing "q" or with Ctrl-<C>.

remove
^^^^^^

Remove a radio information.

Usage:
    ``radio remove [OPTIONS] RADIO_ID``

Options:
  --help  Show this message and exit.

search
^^^^^^

Search radio in the available radios.

Usage:
    ``radio search [OPTIONS] STRING``

Options:
  -i, --invert  Invert filter.
  --help        Show this message and exit.

show
^^^^

Show all radios information.

Usage:
    ``radio show [OPTIONS]``

Options:
  --urls   Also show Streaming URLS.
  --count  Show how many radios are available.
  --help   Show this message and exit

How does it *plays* the radio?
==============================

It requires any of the following media player:

- **ffplayer** (ffmpeg package)
- **cvlc** (vlc package)
- **mplayer**

Priority or alternative players yet to make *customizable* in future versions.

ToDo
====

- support multiples radio lists
- support downloading radio lists from somewhere
- customize player and priorities or autodetect (something like *rifle* in the *ranger* package)
- what more?
- help me at https://github.com/quijot/radio-package

Author
======

* `quijoT <https://github.com/quijot>`_ (Santiago Pestarini <santiagonob@gmail.com>)

Collaborators
-------------

* `sdeancos <https://github.com/sdeancos>`_ (Samuel de Ancos)

License
=======

radio is licensed under the *do What The Fuck you want to Public License*, WTFPL. See the LICENSE file.
