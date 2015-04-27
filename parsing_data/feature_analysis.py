import glob, os
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from heading_analysis import heading_match
from output_color import color_text
# main function
def main_function():
    features_folder = "features"
    story_file = "story.txt"
    # word_tokenize includes puntuations, use this tokenizer instead
    # distintion between U+0027 ('), U+2018 (‘), and U+2019 (’)
    # “ ” "
    print(color_text("starting...", "green"))
    word_tokenizer = RegexpTokenizer(r'(\u0024|\u00A2|\u00A3|\u00A5)?\w+((\u0026|\u0027|\u002C|\u002E|\u003A|\u00B0|\u00E0|\u00E1|\u00E2|\u00E3|\u00E4|\u00E5|\u00E7|\u00E8|\u00E9|\u00EA|\u00EB|\u00EC|\u00ED|\u00EE|\u00EF|\u00F0|\u00F1|\u00F2|\u00F3|\u00F4|\u00F5|\u00F6|\u00F8|\u00F9|\u00FA|\u00FB|\u00FC|\u00FD|\u00FF|\u002D|\u2013|\u2014|\u2019)+\w+)*((\u002B[A-Z])|(\u002F[0-9]+))?\w*(\u0025|\u00B0)?')
    quote_tokenizer = RegexpTokenizer(r'(\u0022|\u201C|\u201D)')
    print('Folder or directory name:')
    folder_name = input("> ")
    os.chdir(folder_name)
    # create features folder
    if not os.path.exists(features_folder):
        os.makedirs(features_folder)
    print(color_text("features folder created...", "blue"))
    # acquire main document lines and headline
    with open(story_file, 'r') as file:
        story_lines = file.readlines()
        story_headline = story_lines[0]
        print(color_text("story text aquired...", "blue"))
    for text_file in glob.glob("d*.txt"):
        file_name = text_file
        new_file = os.path.join(features_folder, file_name[:file_name.index(".txt")] + "_features.txt")
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
            source_lines = file.readlines()
            print(file_name + " text aquired...")
        # collect total paragraphs and sentences from the source file
        total_paras = 0
        total_sents = 0
        for line in source_lines:
            total_paras += 1
            total_sents += len(sent_tokenize(line))
        # write to features files for each source file
        with open(new_file, 'w') as file:
            paras = 0
            sents = 0
            current_quote = 0
            next_quote = 0
            for line in source_lines:
                paras += 1
                source_sentences = sent_tokenize(line)
                weird_quote_sentences = 0
                for source_sentence in source_sentences:
                    sents += 1
                    # figure out if sentence is a quote
                    amount_of_quotations = len(quote_tokenizer.tokenize(source_sentence))
                    start_quote = source_sentence[0] == '\u0022' or source_sentence[0] == '\u201C' or source_sentence[1] == '\u0022' or source_sentence[1] == '\u201C'
                    end_quote = source_sentence[-1] == '\u0022' or source_sentence[-1] == '\u201D' or source_sentence[-2] == '\u0022' or source_sentence[-2] == '\u201D'
                    if amount_of_quotations > 0 and (amount_of_quotations % 2) == 0: # even number of quotes
                        current_quote = 1
                        next_quote = 0
                    elif amount_of_quotations > 0 and end_quote: # odd number with end quote
                        current_quote = 1
                        next_quote = 0
                    elif amount_of_quotations > 0 and start_quote: # odd number with start quote
                        current_quote = 1
                        next_quote = 1
                    elif amount_of_quotations > 0 and next_quote == 1 and end_quote: # odd number with previous sentence odd quote
                        current_quote = 1
                        next_quote = 0
                    elif amount_of_quotations > 0 and next_quote == 0 and start_quote: # odd number with previous sentence even quote or no quote
                        current_quote = 1
                        next_quote = 1
                    elif next_quote == 1: # no quotation in sentence but previous odd quote (start of quote)
                        current_quote = 1
                        weird_quote_sentences += 1
                    else: # no quotations in sentence or previous sentence or even quote in previous sentence
                        current_quote = 0
                        next_quote = 0
                    # sentence id (sent_<id>)
                    # sentence number
                    # total number of sentences
                    # paragraph number
                    # total number of paragraphs
                    # number of words
                    # is sentence a quote (0 - False, 1 - True)
                    # does even one source word from its sentence match story headline (0 - False, 1 - True)
                    #print(source_sentence)
                    #print(story_headline)
                    text = 'sent_' + str(sents) + ", " + str(sents) + ", " + str(total_sents) + ", " + str(paras) + ", " + str(total_paras) + ", " + str(len(word_tokenizer.tokenize(source_sentence))) + ", " + str(current_quote) + ", " + str(heading_match(source_sentence, story_headline, word_tokenizer))
                    #print(text)
                    file.write(text + "\n")
                if weird_quote_sentences > 3:
                    print(color_text("...possible quotation error(s) in " + new_file, "yellow"))
        print("..." + new_file + " file written")
    print(color_text('...done', "green"))
    quit()
# - start here
if __name__ == "__main__":
    main_function()
