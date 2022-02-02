import requests
from bs4 import BeautifulSoup
req  = requests.get("https://vedabase.io/en/library/bg/1/1/")

soup = BeautifulSoup(req.content,"html.parser")


title = soup.title

#print(paras)
#print(soup.prettify())
print(soup.get_text())
