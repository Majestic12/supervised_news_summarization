import urllib.request
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

url = "http://www.bloomberg.com/news/articles/2015-04-17/u-s-antitrust-lawyers-said-to-be-leaning-against-comcast-merger"
html_doc = opener.open(url).read().decode('utf-8')
soup = BeautifulSoup(html_doc)

my_file = open("story3_d1.txt", "w")

head = soup.find_all("span",{"class":"lede-headline__highlighted"})
for heading in head:
    my_file.write(heading.text + ".\n") #add a period to the end of headline

themes = soup.find_all("section",{"class":"article-body"})
for theme in themes:
    for item in theme.find_all("p"):
        my_file.write(item.text + "\n")

my_file.close()
