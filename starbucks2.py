import pandas as pd

starbucks = pd.read_excel('starbucks.xlsx', header = 0)

starbucks.head()

sgg_names = []
for address in starbucks['주소']:
    sgg = address.split()[1]
    sgg_names.append(sgg)

starbucks['시군구명'] = sgg_names

star_sgg_count = starbucks.pivot_table(index = '시군구명', values = "매장명", aggfunc = 'count')
print(star_sgg_count)

