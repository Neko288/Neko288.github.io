import requests
from bs4 import BeautifulSoup
import re
import webbrowser

URL = ('https://nogameb.com/archives/steam-play-for-free.html')
res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")

free_game = soup.find('span', id = 'toc1') 
free_game2 = soup.find('span', id = 'toc2')
"""
free_game3 = soup.find('span', id = 'toc3')
free_game4 = soup.find('span', id = 'toc4')
free_game5 = soup.find('span', id = 'toc5')
free_game6 = soup.find('span', id = 'toc6')
free_game7 = soup.find('span', id = 'toc7')
"""

f = str(free_game.get_text()) 
f2 = str(free_game2.get_text())
"""
f3 = str(free_game3.get_text())
f4 = str(free_game4.get_text())
f5 = str(free_game5.get_text())
f6 = str(free_game6.get_text())
f7 = str(free_game7.get_text())"""
print(f + '\n' + f2)# + '\n' + f3 + '\n' + f4 + '\n' + f5 + '\n' + f6 + '\n' +f7

URL__ = 'https://steamdb.info/upcoming/free/'

input()
webbrowser.open(URL__)