#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json


radio_list_file = os.path.join(os.path.dirname(__file__), 'data/radios.json') 
f = open(radio_list_file)
radio_list = json.load(f)
f.close()


def usage():
    usage = """
    Usage:
    $ radio <radio_id>			Plays radio_id. Press q to quit.
    $ radio -l				Lists available radios.
    $ radio -a radio_id "radio name" url	Add/update radio_id into radio list.
    $ radio -d radio_id			Delete radio_id from radio list.
    """
    return usage


def show_radio_list():
    rl = []
    for radio_id in radio_list:
        if len(radio_id) >= 8:
            tab = '\t'
        else:
            tab = '\t\t'
        rl.append('%s%s%s' % (radio_id, tab, radio_list[radio_id]['name']))
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
        os.system('mplayer %s' % radio_list[radio_id]['url'])
