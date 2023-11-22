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

product_depth = []
product_names = []
product_prices = []
product_urls = []
product_alts = []

# 웹 드라이버 서비스 설정
s = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)
#CU 편의점 url
URL="https://cu.bgfretail.com/event/plus.do?category=event&depth2=1&sf=N"
driver.get(URL)#웹페이지 열기 
time.sleep(1)#대기
# 1+1과 2+1 카테고리
Depth={
    '23':'1+1',
    '24':'2+1',
}

# 카테고리 이동하는 함수
def goDepth(depth):
    script=""
    if depth =='23':
        script = "goDepth('{}')".format(depth)
    elif depth == '24':
        script = "goDepth('{}')".format(depth)
    else:
        script = "goDepth('')"

    driver.execute_script(script) #스크립트 실행
    time.sleep(2)
# 더보기 클릭해서 카테고리 모두 불러오기
def clickMore1(): # 1+1 더보기 모두 클릭
    for i in range(8): # 1+1 8번 2+1 24번
        try:
            driver.execute_script("nextPage(1)")
            time.sleep(2)
        except JavascriptException:
            break
def clickMore2(): # 2+1 더보기 모두 클릭
    for i in range(24): # 1+1 8번 2+1 24번
        try:
            driver.execute_script("nextPage(1)")
            time.sleep(2)
        except JavascriptException:
            break
# 상품정보 가져오는 getProductInfo 함수
def getProductInfo(soup,depth):
    # soup : html parser
    li_element = soup.find_all('li', class_='prod_list')
    for li in li_element:
        # 제품명 추출
        name_element = li.select_one('div.prod_text > div.name > p')
        product_name = name_element.text.strip() # 공백 제거
        product_names.append(product_name) #리스트에 담기
        # 제품가격 추출
        price_element = li.select_one('div.prod_text > div.price > strong')
        product_price = price_element.text.strip()
        product_prices.append(product_price)#리스트에 담기
        #
        img_tag = li.find('img', class_='prod_img')
        if img_tag:# Check if the img tag exists and has an src attribute
            if img_tag.has_attr('src'):
                product_url = img_tag['src'].strip()  # Get the src attribute and strip any extra whitespace
                product_urls.append(product_url)
            if img_tag.has_attr('alt'):
                product_alt = img_tag['alt'].strip()
                product_alt = product_alt.replace('.jpg', '')
                product_alt_cleaned = re.sub(r'[\\/:*?"<>|]', '', product_alt)
                product_alts.append(product_alt_cleaned)

        #메인,서브 카테고리 담기
        product_depth.append(Depth[depth])
        time.sleep(0.3)
#4. 데이터 프레임 생성
# [함수 호출 및 실행 로직]
goDepth('23')  # 1+1 카테고리로 이동
clickMore1()  # 현재 카테고리에서 모든 페이지를 로드
# 현재 페이지의 HTML을 BeautifulSoup 객체로 파싱
soup = BeautifulSoup(driver.page_source, 'html.parser')
getProductInfo(soup, '23') 
goDepth('24') # 2+1 카테고리로 이동
clickMore2() # 현재 카테고리에서 모든 페이지를 로드
# 현재 페이지의 HTML을 BeautifulSoup 객체로 파싱
soup = BeautifulSoup(driver.page_source, 'html.parser')   
getProductInfo(soup, '24')  # 상품 정보 가져오는 함수 호출

# 데이터 프레임 생성
df = pd.DataFrame({
    '행사분류': product_depth,
    '상품명': product_names,
    '가격': product_prices,
    'URL':product_urls,
    "ALT":product_alts,
})

# [코드 6] 여기서 데이터 프레임 수정 및 CSV 파일로 다시 저장
df['가격'] = df['가격'].str.replace(',', '')  # 콤마(,) 제거
df['가격'] = df['가격'].astype(int)  # int 형식으로 변환

# 데이터 프레임 출력
df.to_csv('./CU편의점크롤링.csv', index=False, encoding='cp949', mode='w')

# 드라이버 종료
driver.quit()