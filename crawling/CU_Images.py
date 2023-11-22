import pandas as pd
import requests
from io import BytesIO
import os

# CU편의점크롤링.csv 파일을 읽는다.
df = pd.read_csv('CU편의점크롤링.csv', encoding='cp949')

# 'CU' 폴더가 없으면 생성한다.
if not os.path.exists('../picture/CU'):
    os.makedirs('../picture/CU')

# 각 행에 대해 반복한다.
for index, row in df.iterrows():
    url = row['URL']
    
    # URL이 //로 시작하면 http:를 추가해 주소 형태로 만든다.
    # //로 시작하지 않으면 https://로 시작해 주소로 되어 있다.
    if url.startswith('//'):
        url = 'http:' + url

    # 이미지 다운로드
    response = requests.get(url)
    if response.status_code == 200:
        image = BytesIO(response.content)
        
        # 이미지 파일을 'CU' 폴더에 저장 (ALT 값으로 파일 이름 지정)
        with open(os.path.join('../picture/CU', f"{row['ALT']}.jpg"), 'wb') as file:
            file.write(image.read())
