import requests
from bs4 import BeautifulSoup
def getdata(url):
    r = requests.get(url )
    return r.text

url = "https://vedabase.io/en/library/bg/1/1/"

htmldata = getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')
#print(soup)
data_str = ""
for item in soup.find_all("div", class_="wrapper-devanagari"):
    data_str = data_str + item.get_text()
    for item in soup.find_all("div", class_="wrapper-verse-text"):
         data_str = data_str + item.get_text()
    for item in soup.find_all("div", class_="wrapper-synonyms"):
         data_str = data_str + item.get_text()
    for item in soup.find_all("div", class_="wrapper-translation"):
         data_str = data_str + item.get_text()
    for item in soup.find_all("div", class_="wrapper-puport"):
         data_str = data_str + item.get_text()
print(data_str)



