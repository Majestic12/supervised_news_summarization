# TODO - change so that this accepts a sentence and returns whether the sentence is a quote or not
from nltk.tokenize import sent_tokenize, RegexpTokenizer

def main_function():
    print("starting...")
    tokenizer = RegexpTokenizer(r'(\u0022|\u201C|\u201D)')
    print("Filename")
    file_name = input("> ")
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print("text aquired...")
        current_quote = "False"
        next_quote = "False"
        for line in lines:
            sentences = sent_tokenize(line)
            for sentence in sentences:
                print(sentence)
                amount_of_quotations = len(tokenizer.tokenize(sentence))
                print(str(amount_of_quotations))
                if amount_of_quotations > 0 and (amount_of_quotations % 2) == 0:
                    current_quote = "True"
                elif amount_of_quotations > 0 and next_quote == "True":
                    current_quote = "True"
                    next_quote = "False"
                elif amount_of_quotations > 0 and next_quote == "False":
                    current_quote = "True"
                    next_quote = "True"
                elif next_quote == "True":
                    current_quote = "True"
                else:
                    current_quote = "False"
                print(current_quote)
    print('...done')
    quit()
# - start here
if __name__ == "__main__":
    main_function()
