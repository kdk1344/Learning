# 스타벅스는 어떤 전략으로 매장입지를 선택할까

# 1. 거주인구가 많은 지역에 스타벅스 매장도 많을 것이다.
# 2. 직장인이 많은 지역에 스타벅스 매장도 많을 것이다.

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.starbucks.co.kr/store/store_map.do")

j1_btn = '#container > div > form > fieldset > div > section > article.find_store_cont > article > header.loca_search > h3 > a'
driver.find_element_by_css_selector(j1_btn).click()
time.sleep(0.5)

se_btn =  '#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a'
driver.find_element_by_css_selector(se_btn).click()
time.sleep(0.5)

all_btn = '#mCSB_2_container > ul > li:nth-child(1) > a'
driver.find_element_by_css_selector(all_btn).click()
time.sleep(5)


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

starlist = soup.select("li.quickResultLstCon")

# starstore = starlist[0]
# name = starstore.select('strong')[0].text.strip()
# lat = starstore['data-lat'].strip()
# lng = starstore['data-long'].strip()
# stype = starstore.select('i')[0].text.strip()
# address= str(starstore.select('p.result_details')[0]).split('<br/>')[0].split(">")[1]
# tel = str(starstore.select('p.result_details')[0]).split('<br/>')[1].split("<")[0]

starbucks_list = []
for star in starlist:
    name = star.select('strong')[0].text.strip()
    lat = star['data-lat'].strip()
    lng = star['data-long'].strip()
    stype = star.select('i')[0].text.strip()
    address= str(star.select('p.result_details')[0]).split('<br/>')[0].split(">")[1]
    tel = str(star.select('p.result_details')[0]).split('<br/>')[1].split("<")[0]
    starbucks_list.append([name,lat,lng,stype,address,tel])



columns = ['매장명', '위도', '경도', '매장타입', '주소', '전화번호']
pd_data = pd.DataFrame(starbucks_list, columns = columns)
pd_data.head()
pd_data.info()
pd_data.to_excel('starbucks.xlsx',index=False)