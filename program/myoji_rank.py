import requests
from bs4 import BeautifulSoup
import re

print('あなたの苗字のランキングを教えて上げます')

def myoji_rank():
    myoji = (input('あなたの苗字 : '))#曲名

    res = requests.get('https://myoji-yurai.net/searchResult.htm?myojiKanji=' + myoji)
    myoji_soup = BeautifulSoup(res.content, "lxml")

    rank = myoji_soup.find('p', style = 'font-size:1.2em;margin-bottom:0;') 
    print(rank.text + '\n\n' + '-----------------------------------------------------------' '\n\n')

myoji_rank()

while True:
    myoji_rank()