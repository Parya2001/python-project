import requests
from bs4 import BeautifulSoup as bs
import lxml

def getdata(url):
    r = requests.get(url )
    return r.text

b =[46, 72,43,42,29,47,30,28,34,42,55,20,35,27,20,24,28,78]
y = 1 

url = "https://vedabase.io/en/library/bg/1/1}"
for i in b:
    p=1
    while p!=(i+1):
        url = ("https://vedabase.io/en/library/bg/{}/{}".format(y,p))
        htmldata = getdata(url)
        soup = bs(htmldata, 'html.parser')
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
        p = p+1
    y=y+1
    
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("krishna.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
    
doc_ref = db.collection(u'Bhagavadgita As it is').document(u'chapter 1.1')
doc_ref = db.collection(u'sloka').document(u'verse'),(u'word to word'),(u'translation'),(u'purport')

