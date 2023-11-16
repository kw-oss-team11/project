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

startpage = 2


product_depth = []
product_names = []
product_prices = []
# 웹 드라이버 서비스 설정
s = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)

#CU 편의점 url
URL="https://www.7-eleven.co.kr/product/presentList.asp"
driver.get(URL)#웹페이지 열기 
time.sleep(1)#대기
Depth={
    '1':'1+1',
    '2':'2+1',
}
# [code2]메인 카테고리 분류 
def goDepth(depth):
    script="" #초기화
    if depth =='1': #1+1
        script = "fncTab('{}')".format(depth)

    elif depth == '2': #즉석조리
        script = "fncTab('{}')".format(depth)
    else:
        script = "fncTab('')"

    driver.execute_script(script) #스크립트 실행
    time.sleep(2)

    # [code 4] 더보기 클릭
def clickMore():
    while True:
        try:
            driver.execute_script("fncMore(1)")
            time.sleep(2)
        except JavascriptException:
            break

def getProductInfo(soup,depth):
    #soup :html parser
    # list 추출
    li_elements = soup.find('ul', id='listUl').find_all('li', recursive=False)

    for li in li_elements:
        # Find the 'infowrap' div within each 'li' element
        infowrap = li.find('div', class_='infowrap')
        if infowrap:
            # Find the 'name' div and get its text
            name_div = infowrap.find('div', class_='name')
            product_name = name_div.get_text().strip()
            
            # Find the 'price' div and get its text
            price_div = infowrap.find('div', class_='price')
            product_price = price_div.get_text().strip()
            
            # Append the extracted information to your lists
            product_names.append(product_name)
            product_prices.append(product_price)
            product_depth.append(Depth[depth])
            time.sleep(0.3)

goDepth('1')
clickMore()
soup = BeautifulSoup(driver.page_source, 'html.parser')
getProductInfo(soup, '1')



# 데이터 프레임 생성
df = pd.DataFrame({
    '행사분류': product_depth,
    '상품명': product_names,
    '가격': product_prices
})

# [코드 6] 여기서 데이터 프레임 수정 및 CSV 파일로 다시 저장
df['가격'] = df['가격'].astype(str)  # int 형식으로 변환
df['가격'] = df['가격'].str.replace(',', '')  # 콤마(,) 제거
df['가격'] = df['가격'].astype(int)  # int 형식으로 변환

# 매핑
category_map = {'1': '1+1', '2': '2+1'}
df['ID'] = df['행사분류'].map(category_map)
df['그룹별INDEX'] = df.groupby('ID').cumcount()+1
df['ID'] = df['ID'] + df['그룹별INDEX'].astype(str)
df.set_index('ID', inplace=True)

# 그룹별 INDEX 칼럼 삭제
df.drop('그룹별INDEX', axis=1, inplace=True)

# 데이터 프레임 출력
df.to_csv('./SE편의점크롤링.csv', index=False, encoding='cp949', mode='w')

# 드라이버 종료
driver.quit()
