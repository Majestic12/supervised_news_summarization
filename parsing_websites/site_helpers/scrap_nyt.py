import urllib.request
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

url = "http://www.nytimes.com/2013/06/27/sports/football/patriots-aaron-hernandez-arrested.html"
html_doc = opener.open(url).read().decode('utf-8')
#html_doc = urllib.request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html_doc)

my_file = open("story1_d1.txt", "w")

head = soup.find_all("h1",{"id":"story-heading"})
for heading in head:
    my_file.write(heading.text + ".\n") #add a period to the end of headline


themes = soup.find_all("p",{"class":"story-body-text story-content"})
for theme in themes:
    my_file.write(theme.text + "\n")


my_file.close()
