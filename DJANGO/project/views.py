from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, 'home.html')
def hello_view(request):
    # 'Hello' 문자열을 반환하는 간단한 뷰
    return HttpResponse('Hello')