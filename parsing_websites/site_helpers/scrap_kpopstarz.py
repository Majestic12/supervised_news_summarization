import urllib.request
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

url = "http://www.kpopstarz.com/articles/30677/20130609/star-wars-episode-vii-florence-welch.htm"
html_doc = opener.open(url).read().decode('utf-8')
soup = BeautifulSoup(html_doc)

my_file = open("story2_d2.txt", "w")

head = soup.find_all("h1",{"class":"at_title"})
for heading in head:
    my_file.write(heading.text + ".\n") #add a period to the end of headline

themes = soup.find_all("p")
for theme in themes:
    if not theme.has_attr("style") and not theme.has_attr("class"):
        my_file.write(theme.text + "\n")

my_file.close()
