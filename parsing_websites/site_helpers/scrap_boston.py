import urllib.request
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

url = "http://www.boston.com/news/local/massachusetts/2014/02/26/aaron-hernandez-sued-families-double-shooting-victims/lrZq6gRPOMgiONFnCKSxBO/story.html"
html_doc = opener.open(url).read().decode('utf-8')
#html_doc = urllib.request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html_doc)

my_file = open("story1_d3.txt", "w")

head = soup.find_all("h1",{"class":"content-header__headline"})
for heading in head:
    my_file.write(heading.text + ".\n") #add a period to the end of headline


themes = soup.find_all("p",{"class":"content-text__text"})
for theme in themes:
    my_file.write(theme.text + "\n")


my_file.close()
