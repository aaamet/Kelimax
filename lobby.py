import commands
import generator

i = 0

commands.intro()

commands.options()

while i < 3:
    choice = int(input(" > "))
    if choice == 1:
        generator.start_generator()
    if choice == 2:
        commands.tell_about()
        input("Press Enter to go back to the main menu...")
        commands.terminal_clear()
        commands.banner.banner_centered()
        commands.copyright_text_centered()
        commands.options()
