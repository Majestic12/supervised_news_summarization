import os
if os.name == "nt":
    import windows_console_color as wincolor
#This somewhat depends on what platform you are on.
#The most common way to do this is by printing ANSI escape sequences.
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
#
def print_color_text(some_string, color_type):
    if os.name == "nt":
        reset_color = wincolor.get_text_attr()
        if color_type == "pink":
            wincolor.set_text_attr(wincolor.FOREGROUND_MAGENTA)
        elif color_type == "blue":
            wincolor.set_text_attr(wincolor.FOREGROUND_BLUE)
        elif color_type == "green":
            wincolor.set_text_attr(wincolor.FOREGROUND_GREEN)
        elif color_type == "yellow":
            wincolor.set_text_attr(wincolor.FOREGROUND_YELLOW)
        elif color_type == "red":
            wincolor.set_text_attr(wincolor.FOREGROUND_RED)
        else:
            wincolor.set_text_attr(reset_color)
        print(some_string)
        wincolor.set_text_attr(reset_color)
    else:
        if color_type == "pink":
            print(HEADER + some_string + ENDC)
        elif color_type == "blue":
            print(OKBLUE + some_string + ENDC)
        elif color_type == "green":
            print(OKGREEN + some_string + ENDC)
        elif color_type == "yellow":
            print(WARNING + some_string + ENDC)
        elif color_type == "red":
            print(FAIL + some_string + ENDC)
        else:
            print(ENDC + some_string + ENDC)
