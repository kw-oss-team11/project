from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import csv

@login_required
def home_view(request):
    return render(request, 'home.html')

def gs25(request):
    # GS25에 대한 정보를 렌더링
    file_path = settings.BASE_DIR / 'crawling' / 'GS편의점크롤링.csv'
    with open(file_path, newline='', encoding='cp949') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append({
                '행사분류': row['행사분류'],
                '상품명': row['상품명'],
                '가격': row['가격'],
                'ALT': row['ALT']
            })
    return render(request, 'gs25.html', {'data': data})

def seven(request):
    # SEVEN에 대한 정보를 렌더링
    file_path = settings.BASE_DIR / 'crawling' / 'SE편의점크롤링.csv'
    with open(file_path, newline='', encoding='cp949') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append({
                '행사분류': row['행사분류'],
                '상품명': row['상품명'],
                '가격': row['가격'],
                'ALT': row['ALT']
            })
    return render(request, 'seven.html', {'data': data})

def cu(request):
    # CU에 대한 정보를 렌더링
    file_path = settings.BASE_DIR / 'crawling' / 'CU편의점크롤링.csv'
    with open(file_path, newline='', encoding='cp949') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append({
                '행사분류': row['행사분류'],
                '상품명': row['상품명'],
                '가격': row['가격'],
                'ALT': row['ALT']
            })
    return render(request, 'cu.html', {'data': data})
