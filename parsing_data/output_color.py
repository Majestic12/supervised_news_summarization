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

def color_text(some_string, color_type):
    if color_type == "pink":
        return HEADER + some_string + ENDC
    elif color_type == "blue":
        return OKBLUE + some_string + ENDC
    elif color_type == "green":
        return OKGREEN + some_string + ENDC
    elif color_type == "yellow":
        return WARNING + some_string + ENDC
    elif color_type == "red":
        return FAIL + some_string + ENDC
    elif color_type == "bold":
        return BOLD + some_string + ENDC
    elif color_type == "underline":
        return UNDERLINE + some_string + ENDC
    else:
        return ENDC + some_string + ENDC
