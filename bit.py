from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('chromedriver.exe')
# driver.get("https://news.google.com/covid19/map?hl=ko&mid=%2Fm%2F02j71&gl=KR&ceid=KR%3Ako")
# html = driver.page_source
# soup = BeautifulSoup(html,'html.parser')
# corona = soup.select("table > tbody>tr")
# for i in corona:
#     person = i.select("td")[0].text
#     country = i.select("th > div > div")[1].text
    
#     print(f'{country}의 총 확진자는 {person}이다.')

driver.get("https://search.naver.com/search.naver?query=%EB%AA%A8%EB%B0%94%EC%9D%BC+%EA%B2%8C%EC%9E%84+%EB%A7%A4%EC%B6%9C+%EC%88%9C%EC%9C%84")
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
mobile = soup.select("div.list_info > div")
for m in mobile:
    title = m.select("strong>a")[0].text
    print(rank)
