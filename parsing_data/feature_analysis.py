import glob, os
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from word_analysis import heading_match, noun_match
from entity_analysis import find_named_entity
from console_color import print_color_text
# story refers to cicra text here and source refers to the source documents used in circa
# main function
def main_function():
    features_folder = "features"
    debug_folder = "debug"
    story_file = "story.txt"
    # word_tokenize includes puntuations, use this tokenizer instead
    # distintion between U+0027 ('), U+2018 (‘), and U+2019 (’) - and - U+201C (“), U+201D (”), U+0022 (")
    print_color_text("starting...", "green")
    word_tokenizer = RegexpTokenizer(r'(\u0024|\u00A2|\u00A3|\u00A5)?\w+((\u0026|\u0027|\u002C|\u002E|\u003A|\u00B0|\u00E0|\u00E1|\u00E2|\u00E3|\u00E4|\u00E5|\u00E7|\u00E8|\u00E9|\u00EA|\u00EB|\u00EC|\u00ED|\u00EE|\u00EF|\u00F0|\u00F1|\u00F2|\u00F3|\u00F4|\u00F5|\u00F6|\u00F8|\u00F9|\u00FA|\u00FB|\u00FC|\u00FD|\u00FF|\u002D|\u2013|\u2014|\u2019)+\w+)*((\u002B[A-Z])|(\u002F[0-9]+))?\w*(\u0025|\u00B0)?')
    quote_tokenizer = RegexpTokenizer(r'(\u0022|\u201C|\u201D)')
    print('Folder or directory name:')
    folder_name = input("> ")
    os.chdir(folder_name)
    # create features folder
    if not os.path.exists(features_folder):
        os.makedirs(features_folder)
    print_color_text("features folder created...", "blue")
    # create debug folder
    if not os.path.exists(debug_folder):
        os.makedirs(debug_folder)
    print_color_text("debug folder created...", "blue")
    # acquire main document lines and headline
    with open(story_file, 'r') as file:
        story_lines = file.readlines() # get paragraphs from story.txt
        story_headline = story_lines[0] # get headline from story.txt
        story_lines = story_lines[1:] # get paragraphs except headline from story.txt
        print("story text aquired...")
    story_sentences = []
    for story_line in story_lines:
        story_sentences += sent_tokenize(story_line) # convert story paragraphs into sentences
    # for each source file
    for source_file in glob.glob("d*.txt"):
        file_name = source_file
        features_file = os.path.join(features_folder, file_name[:file_name.index(".txt")] + "_features.txt")
        feature_texts = []
        debug_file = os.path.join(debug_folder, file_name[:file_name.index(".txt")] + "_debug.txt")
        debug_texts = []
        # 'r' - read, 'w' - write, 'a' - append - add to the end, 'r+' - read and write
        # using keyword 'with' to open file - better syntax and exception handling than file open() and close()
        # automatic cleanup after use
        with open(file_name, 'r') as file:
            source_lines = file.readlines() # get paragraphs from source
            source_headline = source_lines[0] # get headline from source
            source_lines = source_lines[1:] # get paragraphs except headline from source
            print(file_name + " text aquired...")
        # collect total paragraphs and sentences from the source file
        total_paras = 0
        total_sents = 0
        for line in source_lines:
            total_paras += 1
            total_sents += len(sent_tokenize(line))
        # write to features files for each source file
        #with open(features_file, 'w') as file:
        paras = 0
        sents = 0
        is_current_quote = 0
        is_next_quote = 0
        for source_line in source_lines:
            paras += 1
            source_sentences = sent_tokenize(source_line)
            weird_quote_sentences = 0
            for source_sentence in source_sentences:
                sents += 1
                # figure out if sentence is a quote
                amount_of_quotations = len(quote_tokenizer.tokenize(source_sentence))
                start_quote = source_sentence[0] == '\u0022' or source_sentence[0] == '\u201C'
                end_quote = source_sentence[-1] == '\u0022' or source_sentence[-1] == '\u201D'
                if len(source_sentence) > 1:
                    start_quote = start_quote or source_sentence[1] == '\u0022' or source_sentence[1] == '\u201C'
                    end_quote = end_quote or source_sentence[-2] == '\u0022' or source_sentence[-2] == '\u201D'
                if amount_of_quotations > 0 and (amount_of_quotations % 2) == 0: # even number of quotes
                    is_current_quote = 1
                    is_next_quote = 0
                elif amount_of_quotations > 0 and end_quote: # odd number with end quote
                    is_current_quote = 1
                    is_next_quote = 0
                elif amount_of_quotations > 0 and start_quote: # odd number with start quote
                    is_current_quote = 1
                    is_next_quote = 1
                elif amount_of_quotations > 0 and is_next_quote == 1 and end_quote: # odd number with previous sentence odd quote
                    is_current_quote = 1
                    is_next_quote = 0
                elif amount_of_quotations > 0 and is_next_quote == 0 and start_quote: # odd number with previous sentence even quote or no quote
                    is_current_quote = 1
                    is_next_quote = 1
                elif is_next_quote == 1: # no quotation in sentence but previous odd quote (start of quote)
                    is_current_quote = 1
                    weird_quote_sentences += 1
                else: # no quotations in sentence or previous sentence or even quote in previous sentence
                    is_current_quote = 0
                    is_next_quote = 0
                # sentence id (sent_<id>)
                sentence_id = 'sent_' + str(sents)
                # sentence number
                # total number of sentences
                # paragraph number
                # total number of paragraphs
                # number of words
                word_count = len(word_tokenizer.tokenize(source_sentence))
                # is sentence a quote (0 - False, 1 - True)
                # number of source words that match source headline
                source_heading_match = heading_match(source_sentence, source_headline, word_tokenizer)
                # number of source words from the source sentence that match story headline
                story_heading_match = heading_match(source_sentence, story_headline, word_tokenizer)
                # number of source words from source sentence that matches the most to a story sentence
                story_sentences_match = noun_match(source_sentence, story_sentences, word_tokenizer)
                # number of named entity using default word tokenize
                # number of named entity using custom word tokenizer
                #print(source_sentence)
                #print(story_headline)
                # collecting both types of named entity quantity
                sentence_entity = find_named_entity(source_sentence, word_tokenizer)
                feature_texts.append(sentence_id + ", " + str(sents) + ", " + str(total_sents) \
                            + ", " + str(paras) + ", " + str(total_paras) \
                            + ", " + str(word_count) + ", " + str(is_current_quote) \
                            + ", " + str(source_heading_match[0]) + ", " + str(story_heading_match[0]) \
                            + ", " + str(story_sentences_match[0]) \
                            + ", " + str(sentence_entity[0]) + ", " + str(sentence_entity[1]))
                #print(text)
                #print("------")
                #print("")
                # debug
                debug_texts.append(sentence_id + ":")
                debug_texts.append(str(sents) + " out of " + str(total_sents) + " sentences")
                debug_texts.append(str(paras) + " out of " + str(total_paras) + " paragraphs")
                if is_current_quote == 0:
                    debug_texts.append("Tagged as not being a quote")
                else:
                    debug_texts.append("Tagged as a quote")
                debug_texts.append("\nHeading Check (Source Sentence and Source Headline Match):")
                debug_texts.append(source_sentence.rstrip('\n'))
                debug_texts.append(source_heading_match[2].rstrip('\n'))
                if source_heading_match[0] > 0:
                    debug_texts.append(str(source_heading_match[0]) + " matches: " + ', '.join(s for s in source_heading_match[1]))
                else:
                    debug_texts.append("no heading matches found")
                debug_texts.append("\nStory Heading Check (Source Sentence and Story Headline Match):")
                debug_texts.append(source_sentence.rstrip('\n'))
                debug_texts.append(story_heading_match[2].rstrip('\n'))
                if story_heading_match[0] > 0:
                    debug_texts.append(str(story_heading_match[0]) + " matches: " + ', '.join(s for s in story_heading_match[1]))
                else:
                    debug_texts.append("no story heading matches found")
                if story_sentences_match[0] > 0:
                    debug_texts.append("\nStory Sentence Check (Source Sentence and Best Story Sentence Match):")
                    debug_texts.append(source_sentence.rstrip('\n'))
                    debug_texts.append(story_sentences_match[2].rstrip('\n'))
                    debug_texts.append(str(story_sentences_match[0]) + " matches: " + ', '.join(s for s in story_sentences_match[1]))
                else:
                    debug_texts.append("\nno story sentence matches found")
                if sentence_entity[0] > 0:
                    debug_texts.append("\nSentence Named Entities using Default Tokenizer:")
                    debug_texts.append(source_sentence.rstrip('\n'))
                    debug_texts.append(str(sentence_entity[0]) + " entities:\n" + ', '.join(s for s in sentence_entity[2]).rstrip('\n'))
                else:
                    debug_texts.append("\nno default named entity found")
                if sentence_entity[1] > 0:
                    debug_texts.append("\nSentence Named Entities using Custom Tokenizer:")
                    debug_texts.append(source_sentence.rstrip('\n'))
                    debug_texts.append(str(sentence_entity[1]) + " entities:\n" + ', '.join(s for s in sentence_entity[3]).rstrip('\n'))
                else:
                    debug_texts.append("\nno custom named entity found")
                debug_texts.append("\n----------------\n")
        # write to features files for each source file
        with open(features_file, 'w') as file:
            for feature_text in feature_texts:
                file.write(feature_text + "\n")
        print("..." + features_file + " file written")
        # write to debug files for each source file
        with open(debug_file, 'w') as file:
            for debug_text in debug_texts:
                file.write(debug_text + "\n")
        print("..." + debug_file + " file written")
        if weird_quote_sentences > 3:
            print_color_text("...possible quotation error(s) in " + features_file, "yellow")
    print_color_text('...done', "green")
    quit()
# - start here
if __name__ == "__main__":
    main_function()
