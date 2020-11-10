import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import json

# 1) 데이터 수집
url = 'http://www.seoul.go.kr/coronaV/coronaStatus.do#status_page_top'
page = urllib.request.urlopen(url)
page = page.read()

# BeautifulSoup 을 활용하여 데이터 가져옴
soup = BeautifulSoup(page, 'html.parser')
seoul_gu = soup.find('div', {'class':'status-confirm'})
corona_gu_total = seoul_gu.get_text()
print(corona_gu_total)

# 구 리스트, 확진자 수 리스트 -> 합치기

'''
corona_gu_total = seoul_gu.get_text()
corona_gu_total = corona_gu_total.split('(')[1]
corona_gu_total = corona_gu_total.split()[0:25]
corona_gu_total

# 2) 데이터 가공
corona_df = pd.DataFrame(corona_gu_total)

corona_df.head()


corona_df = corona_df.rename(columns={0 : 'seoul_gu'})

corona_df['num_corona'] = corona_df['seoul_gu'].str.extract('(\d+)')
corona_df['seoul_gu'] = corona_df['seoul_gu'].str.extract('(\D+)')

corona_df['seoul_gu'] = corona_df['seoul_gu'] + '구'
corona_df['seoul_gu'][23] = '중구'


# 구별 경계선 json 파일
geo_data = 'C:/Users/SEHEE/Downloads/pyVisualization/seoul.json' 
# shp extension -> json extension


with open(geo_data,encoding='utf-8') as f:
    data = json.loads(f.read())

# 행정 구역 경계에 구별 코로나 감염자 수 추가
for i in range(len(corona_df)) : 
    for j in range(len(corona_df)) : 
        if data['features'][i]['properties']["name"] == corona_df["seoul_gu"][j] : 
            data['features'][i]['properties']["corona"] = int(corona_df["num_corona"][j])


corona_df.head()
'''