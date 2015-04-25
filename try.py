from nltk.tokenize import sent_tokenize, RegexpTokenizer

def main_function():
    print("starting...")
    tokenizer = RegexpTokenizer(r'\S+')
    file_name = "crazy.txt"
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print("text aquired...")
        for line in lines:
            sentences = sent_tokenize(line)
            for sentence in sentences:
                print(tokenizer.tokenize(sentence))
    print('...done')
    quit()
# - start here
if __name__ == "__main__":
    main_function()
