import urllib.request
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

url = "http://www.usatoday.com/story/sports/2013/06/26/aaron-hernandez-charged-with-murder/2459751/"
html_doc = opener.open(url).read().decode('utf-8')
#html_doc = urllib.request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html_doc)

my_file = open("story1_d5.txt", "w")

head = soup.find_all("h1",{"class":"asset-headline"})
for heading in head:
    my_file.write(heading.text + ".\n") #add a period to the end of headline


themes = soup.find_all("div",{"class":"asset-double-wide double-wide"})
for theme in themes:
#    try:
#        my_file.write(theme.find_all("p",attr=False).text)
#    except:
#        pass
    #my_file.write(theme.text + "\n")
    #print(theme.find_all("p"))
    for item in theme.find_all("p"):
        if not item.has_attr("class"):
            my_file.write(item.text + "\n")


my_file.close()
