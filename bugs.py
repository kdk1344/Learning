from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome('chromedriver.exe')
# 크롬 브라우저로 인터넷에 연결
driver.get('https://music.bugs.co.kr/chart')
# 멜론 사이트로 접속, 데이터 크롤링

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

song_data = []
rank = 1 # 노래를 담기 위한 리스트와 변수 초기화

songs = soup.select('table.byChart > tbody > tr') # 노래들 100개의 테이블 선택

for song in songs:
    title = song.select('p.title>a')[0].text
    singer = song.select('p.artist>a')[0].text
    song_data.append(['Bugs',rank, title,singer])
    rank += 1
print(song_data)

import pandas as pd

columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns = columns)
pd_data.head()

pd_data.to_excel('bugs.xlsx',index=False)