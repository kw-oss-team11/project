import pandas as pd
import requests
from io import BytesIO
import os

# SE편의점크롤링.csv 파일을 읽는다.
df = pd.read_csv('SE편의점크롤링.csv', encoding='cp949')

# 'SE' 폴더가 없으면 생성한다.
if not os.path.exists('../picture/SE'):
    os.makedirs('../picture/SE')

# 각 행에 대해 반복한다.
for index, row in df.iterrows():
    url = row['URL']
    
    # URL이 /로 시작하면 https://www.7-eleven.co.kr를 추가한다.
    # 세븐일레븐의 경우 위와 같은 주소 형태로 이미지가 저장되어 있다.
    if url.startswith('/'):
        url = 'https://www.7-eleven.co.kr' + url 

    # 이미지 다운로드
    response = requests.get(url)
    if response.status_code == 200:
        image = BytesIO(response.content)
        
        # 이미지 파일을 'SE' 폴더에 저장 (ALT 값으로 파일 이름 지정)
        with open(os.path.join('../picture/SE', f"{row['ALT']}.jpg"), 'wb') as file:
            file.write(image.read())