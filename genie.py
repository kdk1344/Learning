from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.genie.co.kr/chart/top200')

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

song_data = []
rank = 1

songs = soup.select('table>tbody>tr')




for song in songs:
    title = song.select('a.title')[0].text.strip()
    singer = song.select('a.artist')[0].text
    song_data.append(['Genie',rank, title,singer])
    rank += 1


driver.get('https://www.genie.co.kr/chart/top200?pg=2')
html1 = driver.page_source
soup1 = BeautifulSoup(html1,'html.parser')
songs1 = soup1.select('table>tbody>tr')

for song in songs1:
    title = song.select('a.title')[0].text.strip()
    singer = song.select('a.artist')[0].text
    song_data.append(['Genie',rank, title,singer])
    rank += 1

print(song_data)


import pandas as pd

columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns = columns)
pd_data.head()

pd_data.to_excel('genie.xlsx',index=False)