import glob, os
from nltk.tokenize import sent_tokenize, RegexpTokenizer

def main_function():
    features_dir = "features"
    # word_tokenize includes puntuations, use this tokenizer instead
    # distintion between U+0027 ('), U+2018 (‘), and U+2019 (’)
    # “ ” "
    print("starting...")
    tokenizer = RegexpTokenizer(r'(\u0024|\u00A2|\u00A3|\u00A5)?\w+((\u0026|\u0027|\u002C|\u002E|\u003A|\u00B0|\u00E0|\u00E1|\u00E2|\u00E3|\u00E4|\u00E5|\u00E7|\u00E8|\u00E9|\u00EA|\u00EB|\u00EC|\u00ED|\u00EE|\u00EF|\u00F0|\u00F1|\u00F2|\u00F3|\u00F4|\u00F5|\u00F6|\u00F8|\u00F9|\u00FA|\u00FB|\u00FC|\u00FD|\u00FF|\u002D|\u2013|\u2014|\u2019)+\w+)*((\u002B[A-Z])|(\u002F[0-9]+))?\w*(\u0025|\u00B0)?')
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
                    # sentence id (sent_<id>)
                    # sentence number
                    # total number of sentences
                    # paragraph number
                    # total number of paragraphs
                    # number of words
                    text = 'sent' + str(sents) + ", " + str(sents) + ", " + str(total_sents) + ", " + str(paras) + ", " + str(total_paras) + ", " + str(len(tokenizer.tokenize(sentence)))
                    file.write(text + "\n")
        print("...file written")
    print('...done')
    quit()
# - start here
if __name__ == "__main__":
    main_function()
