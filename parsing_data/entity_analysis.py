from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.chunk import ne_chunk
from nltk.tag import pos_tag
from nltk.tree import Tree
#nltk.word_tokenize() - to identify word in a sentence
#nltk.pos_tag()       - to identify the parts of speech
#nltk.ne_chunk()      - to identify Named entities
def find_named_entity(sentence, word_tokenizer):
    # U+0027 (') and U+2019 (’)
    sentence = sentence.replace('\u2019', '\u0027')
    default_count = 0
    default_entity_word = []
    for chunk in ne_chunk(pos_tag(word_tokenize(sentence))):
        if hasattr(chunk, 'label'):
            #print(chunk.label(), ' '.join(c[0] for c in chunk.leaves()))
            default_entity_word.append(chunk.label() + ' ' + ' '.join(c[0] for c in chunk.leaves()))
            default_count += 1
    custom_count = 0
    custom_entity_word = []
    for chunk in ne_chunk(pos_tag(word_tokenizer.tokenize(sentence))):
        if hasattr(chunk, 'label'):
            #print(chunk.label(), ' '.join(c[0] for c in chunk.leaves()))
            custom_entity_word.append(chunk.label() + ' ' + ' '.join(c[0] for c in chunk.leaves()))
            custom_count += 1
    return[default_count, custom_count, default_entity_word, custom_entity_word]
