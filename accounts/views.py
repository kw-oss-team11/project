from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
import csv


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # 로그인 후 리다이렉트할 페이지
        else: print('error')
            # 에러 메시지 반환
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')  # 로그아웃 후 리다이렉트할 페이지

def signup_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')  # 회원가입 후 리다이렉트할 페이지
    return render(request, 'accounts/signup.html', {'form': form})

def display_csv(request):
    file_path = settings.BASE_DIR / 'crawling' / 'CU편의점크롤링.csv'
    with open(file_path, newline='', encoding='cp949') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return render(request, 'accounts/display_csv.html', {'data': data})