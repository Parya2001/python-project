import requests
from bs4 import BeautifulSoup
req = requests.get("https://vedabase.io/en/library/bg/1/1/")
soup: BeautifulSoup = BeautifulSoup(req.content,'html.parser')

sanskrit_verse        = []
english_text          = []
word_to_word_meaning  = []
trans_lation          = []
pur_port              = []

for p in soup.find_all('div', attrs={'class':'col-12'}):
    verse = p.find('div', attrs ={'class':'wrapper-devanagari'})
    print(verse)
    text = p.find('div', attrs ={'class':'wrapper-verse-text'})
    print(text)
    meaning = p.find('div', attrs ={'class':'wrapper-synonyms'})
    print(meaning)
    trans_ = p.find('div', attrs ={'class':'wrapper-translation'})
    print(trans_)
    pur_ = p.find('div', attrs ={'class':'wrapper-puport'})
    print(pur_)

sanskrit_verse.append(verse)
english_text.append(text)
word_to_word_meaning.append(meaning)
trans_lation.append(trans_)
pur_port.append(pur_)

print(sanskrit_verse)
print(english_text)
print(word_to_word_meaning)
print(trans_lation)
print(pur_port)





