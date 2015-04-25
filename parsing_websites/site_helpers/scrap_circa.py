'''
import urllib.request
from bs4 import BeautifulSoup

url = "https://circanews.com/news/apple-pay-milestones-and-competition-1"
html_doc = urllib.request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html_doc)

my_file = open("story4.txt", "w")

head = soup.find_all("h1",{"id":"hero-unit-title"})
for heading in head:
    my_file.write(heading.text + ".\n") #add a period to the end of headline

themes = soup.find_all("div",{"class":"point-comment"})
for theme in themes:
    my_file.write(theme.text + "\n")


quotes = soup.find_all("div",{"class":"point point-quote"})
for quote in quotes:
    for item in quote.find_all("p",{"class":"quote point-comment"}):
        my_file.write('"' + item.text + '"\n')
    for item in quote.find_all("p",{"class":"quote-caption point-comment"}):
        my_file.write(item.text + "\n")

my_file.close()

'''
### Sentence Segmentation & clean-up
my_file = open("story4.txt","r")
raw = my_file.read()
my_file.close()

import nltk
sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
raw_sent = sent_tokenizer.tokenize(raw)

my_file = open("story4_c.txt", "w")
for item in raw_sent:
    my_file.write(item + "\n")
my_file.close()
