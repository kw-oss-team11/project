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
URL="http://gs25.gsretail.com/gscvs/ko/products/event-goods"
driver.get(URL)#웹페이지 열기 
time.sleep(1)#대기
Depth={
    'ONE_TO_ONE':'1+1',
    'TWO_TO_ONE':'2+1',
}

# [code2]메인 카테고리 분류 
def goDepth(depth):
    script="" #초기화
    if depth =='ONE_TO_ONE': #1+1
        element = driver.find_element(By.ID, "ONE_TO_ONE")
        # 요소를 클릭합니다.
        element.click()
    elif depth == 'TWO_TO_ONE': #즉석조리
        element = driver.find_element(By.ID, "TWO_TO_ONE")
        # 요소를 클릭합니다.
        element.click()
    else:
        element = driver.find_element(By.ID, "TOTAL")
        # 요소를 클릭합니다.
        element.click()

    driver.execute_script(script) #스크립트 실행
    time.sleep(2)
    # [code 4] 더보기 클릭
def clickMore(page_number):
    try:
        driver.execute_script(f"goodsPageController.movePage({page_number});")
        time.sleep(2)
    except JavascriptException:
        return
        # [code 5] 상품 정보 가져오기
def getProductInfo(soup,depth):
    #soup :html parser
    # list 추출
    tblwrap_div = soup.find('div', class_='tblwrap mt50')
    # list 만큼 반복
    if tblwrap_div:
        prod_list_ul = tblwrap_div.find('ul', class_='prod_list')
        if prod_list_ul:
            li_elements = prod_list_ul.find_all('li')
            for li in li_elements:
                prod_box_div = li.find('div', class_='prod_box')
                if prod_box_div:
                    name_element = prod_box_div.find('p', class_='tit')
                    if name_element:
                        product_name = name_element.text.strip()
                        product_names.append(product_name)
                    price_element = prod_box_div.find('span', class_='cost')
                    if price_element:
                        product_price = price_element.text.strip()
                        product_prices.append(product_price)
                    product_depth.append(Depth[depth])
                    time.sleep(0.3)

soup = BeautifulSoup(driver.page_source, 'html.parser')
goDepth('ONE_TO_ONE')
soup = BeautifulSoup(driver.page_source, 'html.parser')
last_page_number = int(soup.select_one('a.next2')['onclick'].split('(')[1].split(')')[0])
for page in range(1, last_page_number + 1):
    clickMore(page)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    getProductInfo(soup, 'ONE_TO_ONE')
goDepth('TWO_TO_ONE')
soup = BeautifulSoup(driver.page_source, 'html.parser')
last_page_number = int(soup.select_one('a.next2')['onclick'].split('(')[1].split(')')[0])
for page in range(1, last_page_number + 1):
    clickMore(page)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    getProductInfo(soup, 'TWO_TO_ONE')

# 데이터 프레임 생성
df = pd.DataFrame({
    '행사분류': product_depth,
    '상품명': product_names,
    '가격': product_prices
})

# [코드 6] 여기서 데이터 프레임 수정 및 CSV 파일로 다시 저장
df['가격'] = df['가격'].str.replace(',', '')  # 콤마(,) 제거
df['가격'] = df['가격'].str.replace('원', '')  # 단위(원) 제거
df['가격'] = df['가격'].astype(int)  # int 형식으로 변환

# 매핑
category_map = {'ONE_TO_ONE': '1+1', '2+1': 'b'}
df['ID'] = df['행사분류'].map(category_map)
df['그룹별INDEX'] = df.groupby('ID').cumcount()+1
df['ID'] = df['ID'] + df['그룹별INDEX'].astype(str)
df.set_index('ID', inplace=True)

# 그룹별 INDEX 칼럼 삭제
df.drop('그룹별INDEX', axis=1, inplace=True)

# 데이터 프레임 출력
df.to_csv('./GS편의점크롤링.csv', index=False, encoding='cp949', mode='w')

# 드라이버 종료
driver.quit()
