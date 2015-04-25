import urllib.request
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

url = "http://www.cnn.com/2014/04/29/showbiz/star-wars-cast/"
html_doc = opener.open(url).read().decode('utf-8')
soup = BeautifulSoup(html_doc)

my_file = open("story2_d2.txt", "w")

head = soup.find_all("h1",{"class":"pg-headline"})
for heading in head:
    my_file.write(heading.text + ".\n") #add a period to the end of headline

themes = soup.find_all("p",{"class":"zn-body__paragraph"})
for theme in themes:
    my_file.write(theme.text + "\n")

my_file.close()
