# 멜론 사이트 크롤링

from selenium import webdriver # 웹 연결 - > 크롬
from bs4 import BeautifulSoup  # 분석을하기 위해 html을 정리

driver = webdriver.Chrome('chromedriver.exe')
# 크롬 브라우저로 인터넷에 연결
driver.get('https://www.melon.com/chart/index.htm')
# 멜론 사이트로 접속, 데이터 크롤링

html = driver.page_source

soup = BeautifulSoup(html,'html.parser') # 데이터 정돈 (html)

song_data = []
rank = 1 # 노래를 담기 위한 리스트와 변수 초기화

songs = soup.select('table>tbody>tr') # 노래들 100개의 테이블 선택

for song in songs:
    title = song.select('div.rank01>span>a')[0].text
    singer = song.select('div.rank02>a')[0].text
    song_data.append(['Melon',rank, title,singer])
    rank += 1



import pandas as pd

columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns = columns)
pd_data.head()

pd_data.to_excel('melon.xlsx',index=False)
