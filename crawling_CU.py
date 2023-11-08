from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys # 키 조작
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException#요소가 페이지에 없을때 
from selenium.common.exceptions import JavascriptException

import time #대기시간 지연
import pandas as pd 
from tqdm import tqdm # 진행과정 시각화

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Chrome 옵션 설정
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 필요한 추가 옵션

product_depth = []
product_names = []
product_prices = []
# 웹 드라이버 서비스 설정
s = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)

#CU 편의점 url
URL="https://cu.bgfretail.com/event/plus.do?category=event&depth2=1&sf=N"
driver.get(URL)#웹페이지 열기 
time.sleep(1)#대기
Depth={
    '23':'1+1',
    '24':'2+1',
}

# [code2]메인 카테고리 분류 
def goDepth(depth):
    script="" #초기화
    if depth =='23': #1+1
        script = "goDepth('{}')".format(depth)
    elif depth == '24': #즉석조리
        script = "goDepth('{}')".format(depth)
    else:
        script = "goDepth('')"

    driver.execute_script(script) #스크립트 실행
    time.sleep(2)
    # [code 4] 더보기 클릭
def clickMore():
    for i in range(24): #1+1 8번 2+1 24번
        try:
            driver.execute_script("nextPage(1)")
            time.sleep(2)
        except JavascriptException:
            break
        # [code 5] 상품 정보 가져오기
def getProductInfo(soup,depth):
    #soup :html parser
    # list 추출
    li_element = soup.find_all('li', class_='prod_list')
    # list 만큼 반복
    for li in li_element:
        # 제품명 추출
        name_element = li.select_one('div.prod_text > div.name > p')
        product_name = name_element.text.strip() # 공백 제거
        product_names.append(product_name) #리스트에 담기
        # 제품가격 추출
        price_element = li.select_one('div.prod_text > div.price > strong')
        product_price = price_element.text.strip()
        product_prices.append(product_price)#리스트에 담기
        #메인,서브 카테고리 담기
        product_depth.append(depth)
        time.sleep(0.3)
#4. 데이터 프레임 생성


# [함수 호출 및 실행 로직]
for depth_key, depth_name in Depth.items():
    goDepth(depth_key)  # 메인 카테고리로 이동
    
    clickMore()  # 현재 카테고리에서 모든 페이지를 로드

    # 현재 페이지의 HTML을 BeautifulSoup 객체로 파싱
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    getProductInfo(soup, depth_name)  # 상품 정보 가져오는 함수 호출

# 데이터 프레임 생성
df = pd.DataFrame({
    '행사분류': product_depth,
    '상품명': product_names,
    '가격': product_prices
})

# [코드 6] 여기서 데이터 프레임 수정 및 CSV 파일로 다시 저장
df['가격'] = df['가격'].str.replace(',', '')  # 콤마(,) 제거
df['가격'] = df['가격'].astype(int)  # int 형식으로 변환

# 매핑
category_map = {'1+1': 'a', '2+1': 'b'}
df['ID'] = df['행사분류'].map(category_map)
df['그룹별INDEX'] = df.groupby('ID').cumcount()+1
df['ID'] = df['ID'] + df['그룹별INDEX'].astype(str)
df.set_index('ID', inplace=True)

# 그룹별 INDEX 칼럼 삭제
df.drop('그룹별INDEX', axis=1, inplace=True)

# 데이터 프레임 출력
df.to_csv('./편의점크롤링.csv', index=False, encoding='cp949', mode='w')

# 드라이버 종료
driver.quit()
