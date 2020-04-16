import json
import shutil
import sys
from pathlib import Path

import click

DEFAULT_RADIOS_JSON = Path(__file__).parent / "data" / "radios.json"
CONFIG_DIR = Path.home() / ".config" / "radio"
RADIOS_JSON = CONFIG_DIR / "radios.json"


def load_radios():
    """Load radios from data file (after creating if it does not exists)."""
    if not RADIOS_JSON.exists():
        if not CONFIG_DIR.exists():
            CONFIG_DIR.mkdir()
        with DEFAULT_RADIOS_JSON.open() as f:
            save(json.load(f))
    with RADIOS_JSON.open() as f:
        radios = json.load(f)
    return radios


def save(radios):
    """Save radios to file (after ordering by radio ID)."""
    radios = {rid: radios[rid] for rid in sorted(radios)}
    with RADIOS_JSON.open("w") as f:
        json.dump(radios, f, indent=4)


def find_installed_player():
    """Find an installed player."""
    # find installed player
    if shutil.which("ffplay"):
        player = ["ffplay", "ffplay", "-nodisp"]
    elif shutil.which("cvlc"):
        player = ["cvlc", "cvlc"]
    elif shutil.which("mplayer"):
        player = ["mplayer", "mplayer"]
    else:
        player = None
    return player


def play_url(url):
    """Play an audio streaming url."""
    player = find_installed_player()
    if player is None:
        click.secho("Player NOT found!", fg="red")
        click.secho("Try installing any of the following packages:")
        click.secho("\tffmpeg, vlc or mplayer", bold=True)
        sys.exit(1)
    # launch player
    shutil.os.execlp(*player, url)


def show_list(radios, urls=None, count=None, str_filter="", invert=False):
    if count:
        click.echo(len(radios))
        sys.exit()
    data = "{}{}{name}\n\t\t{url}" if urls else "{}{}{name}"
    for rid, info in radios.items():
        condition = str_filter in rid or str_filter in info["name"].lower()
        condition = not condition if invert else condition
        if condition:
            tab = "\t\t" if len(rid) < 8 else "\t"
            click.secho(data.format(rid, tab, **info))


@click.group(help="Just listen to the radio.")
@click.version_option()
def radio():
    pass


@radio.command(help="Add or update a radio information.", no_args_is_help=True)
@click.option("-n", "--name", required=True, help="Radio complete fancy name.")
@click.option("-u", "--url", required=True, help="Radio playable streaming url.")
@click.argument("radio_id", required=True)
def add(radio_id, name, url):
    radios = load_radios()
    radios[radio_id] = {"name": name, "url": url}
    save(radios)
    click.secho("{} ({}) was succesfully added/updated".format(name, radio_id))


@radio.command(help="Remove a radio information.", no_args_is_help=True)
@click.argument("radio_id", required=True)
def remove(radio_id):
    radios = load_radios()
    if radio_id in radios:
        radio = radios.pop(radio_id)
        save(radios)
        click.secho("{} ({}) was succesfully removed".format(radio["name"], radio_id))
    else:
        click.secho("Radio {} do NOT exists!".format(radio_id), fg="red")


@radio.command(help="Play a radio.", no_args_is_help=True)
@click.argument("radio-id", required=True)
def play(radio_id):
    radios = load_radios()
    if radio_id not in radios:
        click.secho("Radio {} do NOT exists!".format(radio_id), fg="red")
        sys.exit(1)

    click.secho("Playing {name}!".format(**radios[radio_id]), bold=True)
    play_url(radios[radio_id]["url"])


@radio.command(help="Show all radios information.")
@click.option("--urls", is_flag=True, help="Also show Streaming URLS.")
@click.option("--count", is_flag=True, help="Show how many radios are available.")
def show(urls, count):
    radios = load_radios()
    show_list(radios, urls, count)


@radio.command(help="Search radio in the available radios.", no_args_is_help=True)
@click.option("-i", "--invert", is_flag=True, help="Invert filter.")
@click.argument("string", required=True)
def search(string, invert):
    radios = load_radios()
    show_list(radios, str_filter=string.lower(), invert=invert)
