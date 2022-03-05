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
current_v = "v1.2.1"
copyright_text = "Kelimax " + current_v + " Copyright (C) 2022 aaamet"
opt_1 = "1 - Start The Generator - 1"
opt_2 = "2 - Settings - 2"
opt_3 = "3 - About - 3"
opt_4 = "4 - Check For Update - 4"
url = "https://raw.githubusercontent.com/aaamet/version-list/main/kelimax.json"

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

    with open("config.json", "r") as settings:
        data = json.load(settings)
    settings.close()

    if data["delay"] == True:
        intro_delay = "On"
        intro_delay_time = .6
    else:
        intro_delay = "Off"
        intro_delay_time = 0

    terminal_clear()
    banner.banner_centered()
    time.sleep(intro_delay_time)
    copyright_text_centered()
    time.sleep(intro_delay_time)

def options():

    print("")
    print(opt_1.center(shutil.get_terminal_size().columns))
    print(opt_2.center(shutil.get_terminal_size().columns))
    print(opt_3.center(shutil.get_terminal_size().columns))
    print(opt_4.center(shutil.get_terminal_size().columns))

def tell_about():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print(" Kelimax "" Copyright (C) 2022 aaamet")
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

    output_file = open("output.txt", "w")

    with open("config.json", "r") as settings:
        data = json.load(settings)
    settings.close()

    print(" Processing...")



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
    banner.banner_centered()
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
    print(" 1 - Progress Bar (Current position: " + p_bar + ")")
    print("")
    print(" 2 - Intro Delay (Delay between lines of text appearing) (Current position: " + intro_delay + ")")
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
            input(" Press Enter to go back to the main menu...")
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
            input(" Press Enter to go back to the main menu...")
    if setting_choice == "9":
        intro()
        options()

def check_update():

    terminal_clear()

    try:
        print("")
        print(" Checking...")
        print("")
        retrieved = requests.get(url)
        latest_v = retrieved.json()["version"]

        if latest_v == current_v:
            print(" Kelimax is up-to-date! Current version is " + current_v + " .")
            print("")
        else:
            print(" Kelimax is not up-to-date! Please update Kelimax to have the latest bug fixes/features.")
            print("")
            print(" Latest version is " + latest_v +". This version is " + current_v + " .")
            print("")
    except:
        print(" An error occurred. Please check your internet connection and try again.")
        print("")

    input(" Press Enter to go back to the main menu...")
    intro()
    options()
