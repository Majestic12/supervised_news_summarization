#Partial Noun Set Match after Stopwording and Lemmatizing
from nltk.corpus import stopwords
from nltk.corpus.reader.wordnet import ADJ, VERB, NOUN, ADV
from nltk.tokenize import RegexpTokenizer, punkt
from nltk.stem import snowball, wordnet
from nltk.tag import pos_tag
from string import punctuation

target_sentence = "In the eighteenth century it was often convenient to regard man as a clockwork automaton."
sentences = ["In the eighteenth century it was often convenient to regard man as a clockwork automaton.",
             "in the eighteenth century    it was often convenient to regard man as a clockwork automaton",
             "In the eighteenth century, it was often convenient to regard man as a clockwork automaton.",
             "In the eighteenth century, it was not accepted to regard man as a clockwork automaton.",
             "In the eighteenth century, it was often convenient to regard man as clockwork automata.",
             "In the eighteenth century, it was often convenient to regard man as clockwork automatons.",
             "It was convenient to regard man as a clockwork automaton in the eighteenth century.",
             "In the 1700s, it was common to regard man as a clockwork automaton.",
             "In the 1700s, it was convenient to regard man as a clockwork automaton.",
             "In the eighteenth century.",
             "Man as a clockwork automaton.",
             "In past centuries, man was often regarded as a clockwork automaton.",
             "The eighteenth century was characterized by man as a clockwork automaton.",
             "Very long ago in the eighteenth century, many scholars regarded man as merely a clockwork automaton.",]
# Get default English stopwords and extend with punctuation
stop_words = stopwords.words('english')
stop_words.extend(punctuation)
stop_words.append('')
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
# Create tokenizer and stemmer
tokenizer = RegexpTokenizer(r'(\u0024|\u00A2|\u00A3|\u00A5)?\w+((\u0026|\u0027|\u002C|\u002E|\u003A|\u00B0|\u00E0|\u00E1|\u00E2|\u00E3|\u00E4|\u00E5|\u00E7|\u00E8|\u00E9|\u00EA|\u00EB|\u00EC|\u00ED|\u00EE|\u00EF|\u00F0|\u00F1|\u00F2|\u00F3|\u00F4|\u00F5|\u00F6|\u00F8|\u00F9|\u00FA|\u00FB|\u00FC|\u00FD|\u00FF|\u002D|\u2013|\u2014|\u2019)+\w+)*((\u002B[A-Z])|(\u002F[0-9]+))?\w*(\u0025|\u00B0)?')
lemmatizer = wordnet.WordNetLemmatizer()

def is_ci_partial_noun_set_token_stopword_lemma_match(a, b):
    pos_a = map(get_tagged_words, pos_tag(tokenizer.tokenize(a)))
    pos_b = map(get_tagged_words, pos_tag(tokenizer.tokenize(b)))
    lemmae_a = [lemmatizer.lemmatize(token.lower().strip(punctuation), pos) for token, pos in pos_a \
                    if pos == NOUN and token.lower().strip(punctuation) not in stop_words]
    lemmae_b = [lemmatizer.lemmatize(token.lower().strip(punctuation), pos) for token, pos in pos_b \
                    if pos == NOUN and token.lower().strip(punctuation) not in stop_words]
    # Calculate Jaccard similarity
    ratio = len(set(lemmae_a).intersection(lemmae_b)) / float(len(set(lemmae_a).union(lemmae_b)))
    return (ratio > 0.66)

for sentence in sentences:
   print(is_ci_partial_noun_set_token_stopword_lemma_match(target_sentence, sentence), sentence)
