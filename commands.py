import time, os, shutil, textwrap, itertools, json, requests
from tqdm import tqdm

banner_text = """

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
|                       ▄▄   ▄▄                                     |
|▀████▀ ▀███▀         ▀███   ██                                     |
|  ██   ▄█▀             ██                                          |
|  ██ ▄█▀      ▄▄█▀██   ██ ▀███ ▀████████▄█████▄  ▄█▀██▄ ▀██▀   ▀██▀|
|  █████▄     ▄█▀   ██  ██   ██   ██    ██    ██ ██   ██   ▀█▄ ▄█▀  |
|  ██  ███    ██▀▀▀▀▀▀  ██   ██   ██    ██    ██  ▄█████     ███    |
|  ██   ▀██▄  ██▄    ▄  ██   ██   ██    ██    ██ ██   ██   ▄█▀ ▀█▄  |
|▄████▄   ███▄ ▀█████▀▄████▄████▄████  ████  ████▄████▀██▄██▄   ▄██▄|
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄"""
current_v = "v1.3.0"
copyright_text = "Kelimax " + current_v + " Copyright (C) 2022 aaamet"
opt_1 = "1 - Start - 1"
opt_2 = "2 - Settings - 2"
opt_3 = "3 - About - 3"
url = "https://raw.githubusercontent.com/aaamet/version-list/main/kelimax.json"
try:
    retrieved = requests.get(url)
    latest_v = retrieved.json()["version"]
except:
    latest_v = current_v
update = f"(Update available. Latest version: {latest_v})"

def terminal_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner_centered():
    print("")
    print(center_wrap(banner_text, shutil.get_terminal_size().columns))

def copyright_text_centered():
    print("")
    print(copyright_text.center(shutil.get_terminal_size().columns))

def update_check():
    if latest_v != current_v:
        print("")
        print(center_wrap(update, shutil.get_terminal_size().columns))

def intro(d_cancel):

    with open("config.json", "r") as settings:
        data = json.load(settings)
    settings.close()

    if data["delay"] == True:
        intro_delay = "On"
        intro_delay_time = .6
    else:
        intro_delay = "Off"
        intro_delay_time = 0

    if d_cancel == 1:
        intro_delay_time = 0

    terminal_clear()
    banner_centered()
    time.sleep(intro_delay_time)
    copyright_text_centered()
    update_check()
    time.sleep(intro_delay_time)

def options():

    print("")
    print(opt_1.center(shutil.get_terminal_size().columns))
    print(opt_2.center(shutil.get_terminal_size().columns))
    print(opt_3.center(shutil.get_terminal_size().columns))

def main_menu():

    intro(0)
    options()

def tell_about():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print(" Kelimax Copyright (C) 2022 aaamet")
    print("")
    print(" Kelimax is a word list generator that outputs a list of")
    print(" combinations with the given characters.")
    print("")
    print(" It takes three inputs from the user; characters that will")
    print(" be used, minimum and maximum length of the combinations.")
    print("")
    print(" This program is licenced under the terms of GNU General")
    print(" Public Licence v3.0. A copy of the licence can be found")
    print(" in the LICENCE file.")
    print("")

def center_wrap(banner_text_1, cwidth=80, **kw):
    lines = textwrap.wrap(banner_text_1, **kw)
    return "\n".join(line.center(cwidth) for line in lines)

def start_generator():

    characters = input(" Characters > ")
    min_length = int(input(" Minimum Length > "))
    max_length = int(input(" Maximum Length > "))
    print("")

    output_file = open("output.txt", "w")

    with open("config.json", "r") as settings:
        data = json.load(settings)
    settings.close()

    print(" Processing...")
    print("")

    if data["p_bar"] == True:
        for i in tqdm(range(1), desc=" Progress"):
            for n in range(min_length, max_length+1):
                for xs in itertools.product(characters, repeat=n):
                    output_file.write(''.join(map(str, xs)) + "\n")
    else:
        for n in range(min_length, max_length+1):
            for xs in itertools.product(characters, repeat=n):
                output_file.write(''.join(map(str, xs)) + "\n")

    print(" Done!")
    time.sleep(1)
    output_file.close()
    terminal_clear()
    banner_centered()
    copyright_text_centered()
    options()

def settings():

    terminal_clear()

    with open("config.json", "r") as settings:
        data = json.load(settings)
    settings.close()

    if data["p_bar"] == False:
        p_bar = "Off"
    else:
        p_bar = "On"

    if data["delay"] == True:
        intro_delay = "On"
        intro_delay_time = .6
    else:
        intro_delay = "Off"
        intro_delay_time = 0

    print("")
    print(" 1 - Progress Bar (Currently: " + p_bar + ")")
    print("")
    print(" 2 - Intro Delay (Delay between lines of text appearing) (Currently: " + intro_delay + ")")
    print("")
    print(" 9 - Go back to main menu.")
    print("")
    setting_choice = input(" Choose the setting you want to change > ")

    terminal_clear()

    if setting_choice == "1":
        print("")
        set_toggle = input(" Progress Bar - '1' for On, '0' for Off > ")
        if set_toggle == "1" or "0":
            if set_toggle == "1":
                data["p_bar"] = True
                with open("config.json", "w") as settings:
                    json.dump(data, settings)
                settings.close()
            if set_toggle == "0":
                data["p_bar"] = False
                with open("config.json", "w") as settings:
                    json.dump(data, settings)
                settings.close()
            print("")
            print(" Setting has been updated!")
            print("")
            input(" Press Enter to go back to the main menu...")
            main_menu()
    if setting_choice == "2":
        print("")
        set_toggle = input(" Intro Delay - '1' for On, '0' for Off > ")
        if set_toggle == "1" or "0":
            if set_toggle == "1":
                data["delay"] = True
                with open("config.json", "w") as settings:
                    json.dump(data, settings)
                settings.close()
            if set_toggle == "0":
                data["delay"] = False
                with open("config.json", "w") as settings:
                    json.dump(data, settings)
                settings.close()
            print("")
            print(" Setting has been updated!")
            print("")
            input(" Press Enter to go back to the main menu...")
            main_menu()
    if setting_choice == "9":
        intro(0)
        options()
