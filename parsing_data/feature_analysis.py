import glob, os
from nltk.tokenize import sent_tokenize, RegexpTokenizer

def main_function():
    features_dir = "features"
    # word_tokenize includes puntuations, use this tokenizer instead
    # distintion between U+0027 ('), U+2018 (‘), and U+2019 (’)
    # “ ” "
    print("starting...")
    #tokenizer = RegexpTokenizer(r'\S+')
    tokenizer = RegexpTokenizer(r'\$?\w+((\S+)?\w+)*\%?')
    print('Folder or directory name:')
    folder_name = input("> ")
    os.chdir(folder_name)
    if not os.path.exists(features_dir):
        os.makedirs(features_dir)
    print("features folder created...")
    for text_file in glob.glob("*.txt"):
        file_name = text_file
        new_file = os.path.join(features_dir, file_name[:file_name.index(".txt")] + "_features.txt")
        # 'r' - read
        # 'w' - write
        # 'a' - append - add to the end
        # 'r+' - read and write
        #file = open(file_name, 'r')
        # pass arg number to print that many characters
        #print txt.read()
        # loop and read
        #for line in file
            #print(line)
        #file.close()
        # using keyword 'with' to open file
        # better syntax and exception handling than file open() and close()
        # automatic cleanup after use
        with open(file_name, 'r') as file:
            lines = file.readlines()
            print("text aquired...")
        total_paras = 0
        total_sents = 0
        for line in lines:
            total_paras += 1
            total_sents += len(sent_tokenize(line))
        with open(new_file, 'w') as file:
            print("file created...")
            paras = 0
            sents = 0
            for line in lines:
                paras += 1
                sentences = sent_tokenize(line)
                for sentence in sentences:
                    sents += 1
                    # sentence id (sent_<id>), number of words, paragraph number, string number, total number of paragraphs, total number of sentences
                    text = 'sent' + str(sents) + ", " + str(len(tokenizer.tokenize(sentence))) + ", " + str(paras) + ", " + str(sents) + ", " + str(total_paras) + ", " + str(total_sents)
                    file.write(text + "\n")
        print("...file written")
    print('...done')
    quit()
# - start here
if __name__ == "__main__":
    main_function()
