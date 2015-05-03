import glob, os
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer
from nltk.chunk.regexp import RegexpParser
from nltk.tag import pos_tag

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
WORD_TOKENIZER = RegexpTokenizer(r'(\u0024|\u00A2|\u00A3|\u00A5)?\w+((\u0026|\u0027|\u002C|\u002E|\u003A|\u00B0|\u00E0|\u00E1|\u00E2|\u00E3|\u00E4|\u00E5|\u00E7|\u00E8|\u00E9|\u00EA|\u00EB|\u00EC|\u00ED|\u00EE|\u00EF|\u00F0|\u00F1|\u00F2|\u00F3|\u00F4|\u00F5|\u00F6|\u00F8|\u00F9|\u00FA|\u00FB|\u00FC|\u00FD|\u00FF|\u002D|\u2013|\u2014|\u2019)+\w+)*((\u002B[A-Z])|(\u002F[0-9]+))?\w*(\u0025|\u00B0)?')
GRAMMAR = r"""
    NP: {<CD><IN><CD><NN.*>}
        {<DT|CD|PP\$>?<JJ>*<NN.*>+} # chunk determiner/possessive, adjectives and any nouns
    VP: {<V.*>+}
    CU: {<NP>+<VP><NP>+}
        {<NP>+<CC|IN|NP>+<NP>+}
        {<NP>+}
        {<VP>}
"""

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

def get_words(sentence):
    return word_tokenize(sentence)

def get_custom_words(sentence):
    return WORD_TOKENIZER.tokenize(sentence)

def get_pos_words(words_list):
    return pos_tag(words_list)

def apply_grammar(pos_words):
    grammar_parser = RegexpParser(GRAMMAR)
    return grammar_parser.parse(pos_words)

# main function
def chunking_sentence(sentence):
    words_list = get_custom_words(sentence)
    #print(words_list)
    pos_words = get_pos_words(words_list)
    #print(pos_words)
    grammar_words = apply_grammar(pos_words)
    #print(grammar_words)
    np_count = 0
    vp_count = 0
    cu_count = 0
    non_cu_count = 0
    node_count = 0 # cu and non-cu nodes in a sentence
    for grammar_word in grammar_words:
        if hasattr(grammar_word, 'label') and grammar_word.label() == 'CU':
            cu_count += 1
            for grammar_subtree in grammar_word.subtrees():
                if grammar_subtree.label() == 'NP':
                    np_count += 1
                    #print('[ ' + color_text(' '.join(g[0] for g in grammar_subtree.leaves()), "green"), end=' ] ')
                elif grammar_subtree.label() == 'VP':
                    vp_count += 1
                    #print('[ ' + color_text(' '.join(g[0] for g in grammar_subtree.leaves()), "red"), end=' ] ')
            #print('[ ' + color_text(' '.join(g[0] for g in grammar_word.leaves()), "yellow"), end=' ] ')
        else:
            non_cu_count += 1
    node_count = cu_count + non_cu_count
    #print()
    return [np_count, vp_count, cu_count, node_count]

# entry point
if __name__ == "__main__":
    sources_folder = "../sources" # change main folder name here
    features_folder = "features"
    features_add_2 = "_features_add_2.txt"
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
            features_add_file = os.path.join(features_folder, source_file[:source_file.index(".txt")] + features_add_2)
            print("...working on " + source_file)
            with open(source_file, 'r') as file:
                source_lines = file.readlines() # get paragraphs from source
            source_lines = source_lines[1:] # get paragraphs except headline from source
            source_sentences = []
            for source_line in source_lines:
                source_sentences += sent_tokenize(source_line)
            chunk_results = []
            chunk_texts = []
            sent = 0
            for sentence in source_sentences:
                sent += 1
                chunk_results = chunking_sentence(sentence)
                chunk_texts.append("sent_" + str(sent) + ", " + str(chunk_results[0]) + ", " + str(chunk_results[1]) \
                     + ", " + str(chunk_results[2]) + ", " + str(chunk_results[3]))
            # write to features files for each source file
            with open(features_add_file, 'w') as file:
                for chunk_text in chunk_texts:
                    file.write(chunk_text + "\n")
        os.chdir("..")
        print(color_text("Exited folder " + current_folder_name, "pink"))
        print('---------------------------------------------------------------------\n')
    print(color_text('...done', "green"))
    quit()
