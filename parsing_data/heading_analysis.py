#Exact Token Match after Stopwording and Lemmatizing
from nltk.corpus import stopwords
from nltk.corpus.reader.wordnet import ADJ, VERB, NOUN, ADV
from nltk.tokenize import RegexpTokenizer, punkt
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
# check words
def is_exact_word_match(a, b, word_tokenizer, lemmatizer, stop_words):
    pos_a = map(get_tagged_words, pos_tag(word_tokenizer.tokenize(a)))
    pos_b = map(get_tagged_words, pos_tag(word_tokenizer.tokenize(b)))
    lemmae_a = [lemmatizer.lemmatize(token.lower().strip(punctuation), pos) for token, pos in pos_a \
                    if token.lower().strip(punctuation) not in stop_words]
    lemmae_b = [lemmatizer.lemmatize(token.lower().strip(punctuation), pos) for token, pos in pos_b \
                    if token.lower().strip(punctuation) not in stop_words]
    return 1 if (len(set(lemmae_a).intersection(lemmae_b)) > 0) else 0 # if 1 or more word match
# main function
def heading_match(check_sentence, headline_sentence, word_tokenizer):
    # Create tokenizer and stemmer
    lemmatizer = wordnet.WordNetLemmatizer()
    # Get default English stopwords and extend with punctuation
    stop_words = stopwords.words('english')
    stop_words.extend(punctuation)
    stop_words.append('')
    return is_exact_word_match(check_sentence, headline_sentence, word_tokenizer, lemmatizer, stop_words)
