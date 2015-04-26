# TODO - change so that this accepts a sentence and returns number of named entities
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.chunk import ne_chunk
from nltk.tag import pos_tag
from nltk.tree import Tree
#nltk.word_tokenize() - to identify word in a sentence
#nltk.pos_tag()       - to identify the parts of speech
#nltk.ne_chunk()      - to identify Named entities
def main_function():
    tokenizer = RegexpTokenizer(r'(\u0024|\u00A2|\u00A3|\u00A5)?\w+((\u0026|\u0027|\u002C|\u002E|\u003A|\u00B0|\u00E0|\u00E1|\u00E2|\u00E3|\u00E4|\u00E5|\u00E7|\u00E8|\u00E9|\u00EA|\u00EB|\u00EC|\u00ED|\u00EE|\u00EF|\u00F0|\u00F1|\u00F2|\u00F3|\u00F4|\u00F5|\u00F6|\u00F8|\u00F9|\u00FA|\u00FB|\u00FC|\u00FD|\u00FF|\u002D|\u2013|\u2014|\u2019)+\w+)*((\u002B[A-Z])|(\u002F[0-9]+))?\w*(\u0025|\u00B0)?')
    print('file name:')
    file_name = input("> ")
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print("text aquired...")
        for line in lines:
            for sentence in sent_tokenize(line):
                #print(tokenizer.tokenize(sentence))
                #for word in tokenizer.tokenize(sentence):
                    #print(word)
                #chunks = ne_chunk(pos_tag(word_tokenize(sentence)))
                #chunks = ne_chunk(pos_tag(tokenizer.tokenize(sentence)))
                #print(chunks)
                #for chunk in chunks.subtrees():
                    #print(chunk)
                    #if chunk.label().isupper() and chunk.label() != 'S':
                        #print(chunk.label(), ' '.join(c[0] for c in chunk.leaves()))
    print('...done')
    quit()
# - start here
if __name__ == "__main__":
    main_function()
