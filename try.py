import glob, os

def main_function():
    print("starting...")
    print('Folder or directory name:')
    folder_name = input("> ")
    #for sub_folder in os.walk(folder_name):
        #print(next(os.walk('.'))[1])
        #for text_file in glob.glob("d*.txt"):
            #file_name = text_file
            #print(file_name)
    os.walk(folder_name)
    
    quit()
# - start here
if __name__ == "__main__":
    main_function()
