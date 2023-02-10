import commands

i = 0
c = 0

commands.intro(0)
commands.options()

while i < 1:
    choice = input(" > ")
    if choice == "1":
        commands.start_generator()
    if choice == "2":
        commands.settings()
    if choice == "3":
        commands.tell_about()
        input(" Press Enter to go back to the main menu...")
        commands.terminal_clear()
        commands.banner_centered()
        commands.copyright_text_centered()
        commands.options()
    else:
        c += 1
        print(c)
        print("Please enter a valid option.")
        if c == 10:
            commands.intro(1)
            commands.options()
            c = 0
        