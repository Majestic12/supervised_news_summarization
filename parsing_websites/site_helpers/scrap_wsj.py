import urllib.request
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

#url = "http://www.wsj.com/articles/apple-pay-plans-to-launch-in-canada-this-fall-1429280816"
#html_doc = opener.open(url).read().decode('utf-8')

#soup = BeautifulSoup(html_doc)

soup = BeautifulSoup(open("wsj_article.html", encoding="utf8"))

my_file = open("story4_d1.txt", "w")

#head = soup.find_all("h1",{"class":"post-title h-main"})
head = soup.find_all("h1",{"class":"wsj-article-headline"})
for heading in head:
    my_file.write(heading.text + ".\n") #add a period to the end of headline

try:
    head2 = soup.find_all("h2",{"class":"sub-head"})
    for heading2 in head2:
        my_file.write(heading2.text + ".\n")
except:
    pass


#themes = soup.find_all("div",{"class":"post-content"})
themes = soup.find_all("div",{"id":"wsj-article-wrap"})

for theme in themes:
    for item in theme.find_all("p"):
        my_file.write(item.text + "\n")

my_file.close()
