from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import JavascriptException

import time #대기시간 지연
import pandas as pd 
import re

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Chrome 옵션 설정
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 필요한 추가 옵션

startpage = 2


product_depth = []
product_names = []
product_prices = []
product_urls = []
product_alts = []
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

def clickMore1():
    for i in range(40):
        try:
            driver.execute_script("fncMore(1)")
            time.sleep(2)
        except JavascriptException:
            print('igo')
            break
        except Exception as e:
            print('igo')
            break
def clickMore2():
    for i in range(95):
        try:
            driver.execute_script("fncMore(2)")
            time.sleep(2)
        except JavascriptException:
            print('igo')
            break
        except Exception as e:
            print('igo')
            break
        # [code 5] 상품 정보 가져오기

def getProductInfo(soup,depth):
    #soup :html parser
    # list 추출
    li_elements = soup.find('ul', id='listUl').find_all('li', recursive=False)

    for li in li_elements:
        # Find the 'infowrap' div within each 'li' element
        infowrap = li.find('div', class_='infowrap')
        pic_product = li.find('div', class_='pic_product')
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
        if pic_product:
            img = pic_product.find('img')
            if img:
                if img.has_attr('src'):
                    product_url = img['src'].strip()
                    product_urls.append(product_url)
                if img.has_attr('alt'):
                    product_alt = img['alt'].strip()
                    product_alt_cleaned = re.sub(r'[\\/:*?"<>|]', '', product_alt)
                    product_alts.append(product_alt_cleaned)

        

#SEVEN은 7-eleven.co.kr 붙이면 됨


goDepth('1')
clickMore1()
soup = BeautifulSoup(driver.page_source, 'html.parser')
getProductInfo(soup, '1')
goDepth('2')
clickMore2()
soup = BeautifulSoup(driver.page_source, 'html.parser')
getProductInfo(soup, '2')


# 데이터 프레임 생성
df = pd.DataFrame({
    '행사분류': product_depth,
    '상품명': product_names,
    '가격': product_prices,
    'URL':product_urls,
    "ALT":product_alts,
})

# [코드 6] 여기서 데이터 프레임 수정 및 CSV 파일로 다시 저장
df['행사분류'] = df['행사분류'].replace(1, '1+1')
df['가격'] = df['가격'].str.replace(',', '')  # 콤마(,) 제거
df['가격'] = df['가격'].str.replace('원', '')  # 단위(원) 제거
df['가격'] = df['가격'].astype(int)  # int 형식으로 변환

# 데이터 프레임 출력
df.to_csv('./SE편의점크롤링.csv', index=False, encoding='cp949', mode='w')

# 드라이버 종료
driver.quit()