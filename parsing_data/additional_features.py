import glob, os
from nltk.tokenize import RegexpTokenizer, sent_tokenize
from nltk.tag import pos_tag
#NOTE only works on unix platforms that accept ascii codes
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
    else:
        return ENDC + some_string + ENDC
# main function
def pos_words(check_sentence):
    word_tokenizer = RegexpTokenizer(r'(\u0024|\u00A2|\u00A3|\u00A5)?\w+((\u0026|\u0027|\u002C|\u002E|\u003A|\u00B0|\u00E0|\u00E1|\u00E2|\u00E3|\u00E4|\u00E5|\u00E7|\u00E8|\u00E9|\u00EA|\u00EB|\u00EC|\u00ED|\u00EE|\u00EF|\u00F0|\u00F1|\u00F2|\u00F3|\u00F4|\u00F5|\u00F6|\u00F8|\u00F9|\u00FA|\u00FB|\u00FC|\u00FD|\u00FF|\u002D|\u2013|\u2014|\u2019)+\w+)*((\u002B[A-Z])|(\u002F[0-9]+))?\w*(\u0025|\u00B0)?')
    # number of words that contain a number
    count_num = 0
    # number of words that are capitalized
    count_cap = 0
    # number of nouns in the sentence
    count_noun = 0
    # number of verbs in the sentence
    count_verb = 0
    # number of adjectives in the sentence
    count_adj = 0
    # number of adverbs in the sentence
    count_adv = 0
    # number of prepositions in the sentence
    count_pp = 0
    # number of conjuctions in the sentence
    count_cc = 0
    for token, pos in pos_tag(word_tokenizer.tokenize(check_sentence)):
        if any(char.isdigit() for char in token):
            count_num += 1

        if token[0].isupper():
            count_cap += 1

        if pos.startswith('N'): # noun
            #print(color_text(token, "blue"), end=' ')
            count_noun += 1
        elif pos.startswith('V'): # verb
            #print(color_text(token, "red"), end=' ')
            count_verb += 1
        elif pos.startswith('J'): # adjective
            #print(color_text(token, "pink"), end=' ')
            count_adj += 1
        elif pos.startswith('R'): # adverb
            #print(color_text(token, "green"), end=' ')
            count_adv += 1
        elif pos.startswith('IN'): # preposition
            #print(color_text(token, "yellow"), end=' ')
            count_pp += 1
        elif pos.startswith('CC'): # conjunction
            #print(color_text(token, "yellow"), end=' ')
            count_cc += 1
    #print()
    count_cap = 0 if count_cap <= 1 else (count_cap - 1) # ignore first word capitalized
    #print('number of capitalized words: ' + str(count_cap))
    #print('number of numbered words: ' + str(count_num))
    return [count_num, count_cap, count_noun, count_verb, count_adj, count_adv, count_pp, count_cc]
# - start here
if __name__ == "__main__":
    sources_folder = "../sources" # change main folder name here
    features_folder = "features"
    print(color_text("starting...", "green"))
    sources_sub_folders = next(os.walk(sources_folder))[1]
    os.chdir(sources_folder)
    for folder_name in sources_sub_folders:
        os.chdir(folder_name)
        current_folder_path, current_folder_name = os.path.split(os.getcwd())
        print(color_text("Entered folder " + current_folder_name, "pink"))
        # create features folder
        if os.path.exists(features_folder):
            print(color_text("features folder already exists", "yellow"))
        else:
            os.makedirs(features_folder)
            print(color_text("features folder created...", "blue"))
        for source_file in glob.glob("d*.txt"):
            features_add_file = os.path.join(features_folder, source_file[:source_file.index(".txt")] + "_features_add_1.txt")
            print("...working on " + source_file)
            with open(source_file, 'r') as file:
                source_lines = file.readlines() # get paragraphs from source
            source_lines = source_lines[1:] # get paragraphs except headline from source
            source_sentences = []
            for source_line in source_lines:
                source_sentences += sent_tokenize(source_line)
            pos_array = []
            pos_texts = []
            sent = 0
            for source_sentence in source_sentences:
                sent += 1
                pos_array = pos_words(source_sentence)
                pos_texts.append("sent_" + str(sent) + ", " + str(pos_array[0]) + ", " + str(pos_array[1]) \
                    + ", " + str(pos_array[2]) + ", " + str(pos_array[3]) + ", " + str(pos_array[4]) \
                    + ", " + str(pos_array[5]) + ", " + str(pos_array[6]) + ", " + str(pos_array[7]))
            # write to features files for each source file
            with open(features_add_file, 'w') as file:
                for pos_text in pos_texts:
                    file.write(pos_text + "\n")
        os.chdir("..")
        print(color_text("Exited folder " + current_folder_name, "pink"))
        print('---------------------------------------------------------------------\n')
    print(color_text('...done', "green"))
    quit()
