import pandas as pd
import requests
from io import BytesIO
import os

# GS편의점크롤링.csv 파일을 읽는다.
df = pd.read_csv('GS편의점크롤링.csv', encoding='cp949')

# 'GS' 폴더가 없으면 생성한다.
if not os.path.exists('../picture/GS'):
    os.makedirs('../picture/GS')

# 각 행에 대해 반복한다.
for index, row in df.iterrows():
    url = row['URL']
    if url == '0':
        #이미지가 없는 경우 0을 넣었기 때문에 생긴 조건문
        continue

    # GS의 경우 주소 형식으로 되어 있어 변환이 필요 없다.

    # 이미지 다운로드
    response = requests.get(url)
    if response.status_code == 200:
        image = BytesIO(response.content)
        
        # 이미지 파일을 'GS' 폴더에 저장 (ALT 값으로 파일 이름 지정)
        with open(os.path.join('../picture/GS', f"{row['ALT']}.jpg"), 'wb') as file:
            file.write(image.read())
