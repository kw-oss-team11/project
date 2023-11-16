from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, 'home.html')
def gs25(request):
    # GS25에 대한 정보를 렌더링
    return render(request, 'gs25.html')

def seven(request):
    # SEVEN에 대한 정보를 렌더링
    return render(request, 'seven.html')

def cu(request):
    # CU에 대한 정보를 렌더링
    return render(request, 'cu.html')
