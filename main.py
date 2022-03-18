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

page = 1
titles = []
while page != 35:
      url = f"https://vedabase.io/en/library/bg/1/1/?page={page}"
      response = requests.get(url)
      html = response.content
      soup = bs(html, "lxml")
      for h3 in soup.find_all("h2", class_="wrapper devnagari"):
            titles.append(h3.get_text(strip=True))
      page = page + 1
