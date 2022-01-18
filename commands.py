import time
import os
import shutil
import textwrap

banner_text = """

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
|                       ▄▄   ▄▄                                     |
|▀████▀ ▀███▀         ▀███   ██                                     |
|  ██   ▄█▀             ██                                          |
|  ██ ▄█▀      ▄▄█▀██   ██ ▀███ ▀████████▄█████▄  ▄█▀██▄ ▀██▀   ▀██▀|
|  █████▄     ▄█▀   ██  ██   ██   ██    ██    ██ ██   ██   ▀██ ▄█▀  |
|  ██  ███    ██▀▀▀▀▀▀  ██   ██   ██    ██    ██  ▄█████     ███    |
|  ██   ▀██▄  ██▄    ▄  ██   ██   ██    ██    ██ ██   ██   ▄█▀ ██▄  |
|▄████▄   ███▄ ▀█████▀▄████▄████▄████  ████  ████▄████▀██▄██▄   ▄██▄|
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄"""
copyright_text = "Kelimax Copyright (C) 2022 aaamet"
opt_1 = "1 - Start The Generator - 1"
opt_2 = "2 - About - 2"

def terminal_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class banner():

    def banner_centered():
        print("")
        print(center_wrap(banner_text, shutil.get_terminal_size().columns))

    def banner_yclean():

        terminal_clear()
        banner_centered()
        print("")
        copyright_text_centered()
        print("")

    def banner_nclean():

        banner_centered()
        print("")
        copyright_text_centered()
        print("")

def copyright_text_centered():
    print("")
    print(copyright_text.center(shutil.get_terminal_size().columns))

def intro():

    terminal_clear()
    banner.banner_centered()
    time.sleep(.75)
    copyright_text_centered()
    time.sleep(.5)

def options():

    print("")
    print(opt_1.center(shutil.get_terminal_size().columns))
    print(opt_2.center(shutil.get_terminal_size().columns))

def tell_about():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("Kelimax Copyright (C) 2022 aaamet")
    print("")
    print("Kelimax is a word list generator that outputs a list of")
    print("combinations with the given characters.")
    print("")
    print("It takes three inputs from the user; characters that will")
    print("be used, minimum and maximum length of the combinations.")
    print("")
    print("This program is licenced under the terms of GNU General")
    print("Public Licence v3.0. A copy of the licence can be found")
    print("in the LICENCE file.")
    print("")

def center_wrap(banner_text_1, cwidth=80, **kw):
    lines = textwrap.wrap(banner_text_1, **kw)
    return "\n".join(line.center(cwidth) for line in lines)
