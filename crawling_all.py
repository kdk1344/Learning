from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('chromedriver.exe')

def Songs(site,t):
    driver.get(site)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    songs = soup.select(t)
    return songs

def Song_data(songs,company,num,t1,t2):
    song_data = []
    rank = num
    for song in songs:
        title = song.select(t1)[0].text.strip()
        singer = song.select(t2)[0].text
        song_data.append([company,rank, title,singer])
        rank += 1
    return song_data

M = Songs('https://www.melon.com/chart/index.htm', 'table>tbody>tr')
Melon = Song_data(M, 'Melon', 1, 'div.rank01>span>a','div.rank02>a')
B = Songs('https://music.bugs.co.kr/chart', 'table.byChart>tbody>tr')
Bugs = Song_data(B, 'Bugs', 1, 'p.title>a','p.artist>a')
G1 = Songs('https://www.genie.co.kr/chart/top200', 'table>tbody>tr')
Genie1 = Song_data(G1, 'Genie', 1, 'a.title','a.artist')
G2 = Songs('https://www.genie.co.kr/chart/top200a?pg=2', 'table>tbody>tr')
Genie2 = Song_data(G2, 'Genie', 51, 'a.title','.artist')
Genie = Genie1 + Genie2

A = Melon + [[]] +Bugs + [[]] + Genie

columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(A, columns = columns)
pd_data.head()
pd_data.to_excel('crawling.xlsx',index=False)

