import glob, os
#NOTE only works on unix platforms that accept ascii codes
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
# apply asci color codes
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
    else:
        return ENDC + some_string + ENDC
# main function
def rename_files_in_folder(folder_name, features_folder):
    os.chdir(folder_name)
    current_folder_path, current_folder_name = os.path.split(os.getcwd())
    print(color_text("Entered folder " + current_folder_name, "pink"))
    print("Enter Story Number:")
    source_number = input("> ")
    os.chdir(features_folder)
    current_folder_path, current_folder_name = os.path.split(os.getcwd())
    print(color_text("Entered folder " + current_folder_name, "blue"))
    for source_file in glob.glob("doc*.txt"):
        file_basename = source_file[:source_file.index(".txt")]
        doc_number = file_basename[4:file_basename.index("_features")]
        rename_name = "s" + source_number + "d" + doc_number
        if file_basename.endswith("features"):
            os.rename(source_file, rename_name + ".txt")
        elif file_basename.endswith("_add_1"):
            os.rename(source_file, rename_name + "_1.txt")
        elif file_basename.endswith("_add_2"):
            os.rename(source_file, rename_name + "_2.txt")
    os.chdir("../..")
    current_folder_path, current_folder_name = os.path.split(os.getcwd())
    print(color_text("Exited to " + current_folder_name, "pink"))
    print('---------------------------------------------------------------------\n')
# - entry point
if __name__ == "__main__":
    sources_folder = "classifiers/data_test" # change main folder name here
    features_folder = "features"
    print(color_text("starting...", "green"))
    sources_sub_folders = next(os.walk(sources_folder))[1]
    os.chdir(sources_folder)
    for folder_name in sources_sub_folders:
        rename_files_in_folder(folder_name, features_folder)
    print(color_text('...done', "green"))
    quit()
