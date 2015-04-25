from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.chunk import ne_chunk
from nltk.tag import pos_tag
from nltk.tree import Tree
#nltk.word_tokenize() - to identify word in a sentence
#nltk.pos_tag()       - to identify the parts of speech
#nltk.ne_chunk()      - to identify Named entities
def main_function():
    tokenizer = RegexpTokenizer(r'\$?\w+((\S+)?\w+)*\%?')
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
                chunks = ne_chunk(pos_tag(tokenizer.tokenize(sentence)))
                #print(chunks)
                for chunk in chunks.subtrees():
                    print(chunk)
                    #if chunk.label().isupper() and chunk.label() != 'S':
                        #print(chunk.label(), ' '.join(c[0] for c in chunk.leaves()))
    #for line in lines:
        #
    #with open(new_file, 'w') as file:
        #print("file created...")
        #for line in lines:
            #sentences = sent_tokenize(line)
            #for sentence in sentences:
                #file.write(text + "\n")
    #print("...file written")
    print('...done')
    quit()
# - start here
if __name__ == "__main__":
    main_function()
