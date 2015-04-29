from nltk.corpus import stopwords
from nltk.corpus.reader.wordnet import ADJ, VERB, NOUN, ADV
from nltk.tokenize import sent_tokenize, RegexpTokenizer, punkt
from nltk.stem import wordnet
from nltk.tag import pos_tag
from string import punctuation
# check if word is a part of speech
def get_tagged_words(tag_word):
    if tag_word[1].startswith('J'):
        return (tag_word[0], ADJ)
    elif tag_word[1].startswith('V'):
        return (tag_word[0], VERB)
    elif tag_word[1].startswith('N'):
        return (tag_word[0], NOUN)
    elif tag_word[1].startswith('R'):
        return (tag_word[0], ADV)
    else:
        return (tag_word[0], NOUN)
# number of exact word match between two sentences after stripping out punctuations, stopwords and with lemmatizing
def number_of_exact_word_match(a, b, word_tokenizer, lemmatizer, stop_words):
    pos_a = map(get_tagged_words, pos_tag(word_tokenizer.tokenize(a)))
    pos_b = map(get_tagged_words, pos_tag(word_tokenizer.tokenize(b)))
    lemmae_a = [lemmatizer.lemmatize(token.lower().strip(punctuation), pos) for token, pos in pos_a \
                    if token.lower().strip(punctuation) not in stop_words]
    lemmae_b = [lemmatizer.lemmatize(token.lower().strip(punctuation), pos) for token, pos in pos_b \
                    if token.lower().strip(punctuation) not in stop_words]
    matched_words = set(lemmae_a).intersection(lemmae_b)
    return [len(matched_words), matched_words, b]
# number of noun (partial) match between two sentences after stripping out punctuations, stopwords and with lemmatizing
def number_of_noun_match(a, b, word_tokenizer, lemmatizer, stop_words):
    pos_a = map(get_tagged_words, pos_tag(word_tokenizer.tokenize(a)))
    pos_b = map(get_tagged_words, pos_tag(word_tokenizer.tokenize(b)))
    lemmae_a = [lemmatizer.lemmatize(token.lower().strip(punctuation), pos) for token, pos in pos_a \
                    if pos == NOUN and token.lower().strip(punctuation) not in stop_words]
    lemmae_b = [lemmatizer.lemmatize(token.lower().strip(punctuation), pos) for token, pos in pos_b \
                    if pos == NOUN and token.lower().strip(punctuation) not in stop_words]
    # Calculate Jaccard similarity
    #ratio = len(set(lemmae_a).intersection(lemmae_b)) / float(len(set(lemmae_a).union(lemmae_b)))
    #return (ratio > 0.66)
    matched_words = set(lemmae_a).intersection(lemmae_b)
    return [len(matched_words), matched_words, b]
#Exact Token Match after Stopwording and Lemmatizing
def heading_match(check_sentence, headline_sentence, word_tokenizer):
    # Create tokenizer and stemmer
    lemmatizer = wordnet.WordNetLemmatizer()
    # Get default English stopwords and extend with punctuation
    stop_words = stopwords.words('english')
    stop_words.extend(punctuation)
    stop_words.append('')
    return_matches = number_of_exact_word_match(check_sentence, headline_sentence, word_tokenizer, lemmatizer, stop_words)
    #if return_matches[0] > 0:
        #print(return_matches[1])
    return return_matches
#Partial Noun Set Match after Stopwording and Lemmatizing
# NOTE: using exact word instead of partial
def noun_match(check_sentence, story_sentences, word_tokenizer):
    # Create tokenizer and stemmer
    lemmatizer = wordnet.WordNetLemmatizer()
    # Get default English stopwords and extend with punctuation
    stop_words = stopwords.words('english')
    stop_words.extend(punctuation)
    stop_words.append('')
    max_match = [0, "", ""]
    for story_sentence in story_sentences:
        noun_match = number_of_exact_word_match(check_sentence, story_sentence, word_tokenizer, lemmatizer, stop_words)
        max_match = noun_match if noun_match[0] > max_match[0] else max_match
    #if max_match[0] > 0:
        #print(max_match[1], " ", max_match[2])
    return max_match
