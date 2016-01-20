#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json
import distutils.spawn


radio_list_file = os.path.join(os.path.dirname(__file__), 'data/radios.json') 
f = open(radio_list_file)
radio_list = json.load(f)
f.close()

__version__ = '0.0.11'

def version():
    return __version__


def usage():
    usage = """Usage:
    
    $ radio radio_id            Play radio_id. Press <q> or Ctrl-<C> to quit.
    $ radio [-h|--help]         Show this usage help.
    $ radio -l|--list           List available radios.
    $ radio --list-all          List available radios and their urls.
    $ radio --add radio_id "radio name" url
                                Add/update radio_id into radio list.
    $ radio --remove radio_id   Remove radio_id from radio list.
    $ radio [-v|--version]	Show version number.
    """
    return usage


def show_radio_list(urls=False):
    rl = []
    for radio_id in radio_list:
        if len(radio_id) >= 8:
            tab = '\t'
        else:
            tab = '\t\t'
        rl.append('%s%s%s%s' % (radio_id, tab, radio_list[radio_id]['name'], '\n\t\t%s' % radio_list[radio_id]['url'] if urls else ''))
        rl.sort()
    for r in rl: print(r)


def __save():
    f = open(radio_list_file, 'w')
    json.dump(radio_list, f, indent=4)
    f.close()


def add(radio_id, radio_name, radio_url):
    radio_list[radio_id] = {'name': radio_name, 'url': radio_url}
    __save()


def delete(radio_id):
    del radio_list[radio_id]
    __save()


def play(radio_id):
    if radio_list.get(radio_id, 'error') == 'error':
        print(usage())
    else:
        if distutils.spawn.find_executable('mplayer'):
            os.system('mplayer %s' % radio_list[radio_id]['url'])
        elif distutils.spawn.find_executable('ffplay'):
            os.system('ffplay -nodisp %s' % radio_list[radio_id]['url'])
        elif distutils.spawn.find_executable('cvlc'):
            os.system('cvlc %s' % radio_list[radio_id]['url'])
        else:
            print('Player not found')

