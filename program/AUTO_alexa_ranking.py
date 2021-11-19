import requests
from bs4 import BeautifulSoup
import re
import pyperclip

#This is AUTO version

"""#クリップボードに . が含まれいるか判断
if '.' in pyperclip.paste():
    want_URL = pyperclip.paste()"""
def alexa_rank():
    want_URL = (input('please URL : '))  

    URL = ('https://www.alexa.com/siteinfo/' + want_URL)
    res = requests.get(URL)
    print('loading...')
    soup = BeautifulSoup(res.text, "html.parser")

    ranking = soup.find('p', class_='big data') #big dateというclassにランキング情報in
    ranking = re.sub('[<p class="big data"> <span class="hash">#</span> </p>]', ' ', ranking.text) #ここでspanなど不要な情報を削除


    print(want_URL + '\n    global rank #' + ranking.strip())#stripでスペースと改行を削除

    Source = ('\nFor more :' + URL + '\n\n')
    print(Source)

while True:
    alexa_rank()