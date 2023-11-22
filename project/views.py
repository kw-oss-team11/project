from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import csv
from .forms import QueryForm
import qrcode
import random
import pandas as pd
from io import BytesIO
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
def generate_qr(request):
    # 현재 로그인한 사용자의 username 가져오기
    data = request.user.username if request.user.is_authenticated else "꺄륵꺄륵"

    # 나머지 코드는 동일
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    response = HttpResponse(content_type="image/png")
    img_io = BytesIO()
    img.save(img_io, format='PNG')
    img_io.seek(0)
    response.write(img_io.read())

    return response


rule_path = settings.BASE_DIR / 'crawling' / 'chatbot_rule.xlsx'
chatbot_data = pd.read_excel(rule_path)
GS_file_path = settings.BASE_DIR / 'crawling' / 'GS편의점크롤링.csv'
SE_file_path = settings.BASE_DIR / 'crawling' / 'SE편의점크롤링.csv'
CU_file_path = settings.BASE_DIR / 'crawling' / 'CU편의점크롤링.csv'
cu_data=pd.read_csv(CU_file_path, encoding='cp949')
gs_data=pd.read_csv(GS_file_path, encoding='cp949')
se_data=pd.read_csv(SE_file_path, encoding='cp949')

def gptans(request):
    # 폼을 인스턴스화해서 템플릿으로 전달
    form = QueryForm()

    if request.method == 'POST':
        # POST 요청인 경우 폼에서 전송된 데이터를 사용하여 연산 수행
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            if "CU" in query or "GS" in query or "세븐" in query or "cu" in query or "gs" in query:
                if ("CU" in query and "1+1" in query) or ("cu" in query and "1+1" in query):
                    result = event(cu_data, "1+1")
                elif ("GS" in query and "1+1" in query) or ("gs" in query and "1+1" in query):
                    result = event(gs_data, "1+1")
                elif "세븐" in query and "1+1" in query:
                    result = event(se_data, "1+1")
                elif ("CU" in query and "2+1" in query) or ("cu" in query and "2+1" in query):
                    result = event(cu_data, "2+1")
                elif ("GS" in query and "2+1" in query) or ("gs" in query and "2+1" in query):
                    result = event(gs_data, "2+1")
                elif "세븐" in query and "2+1" in query:
                    result = event(se_data, "2+1")
                else:
                    result= "조금 더 자세히 물어봐주세요!"
            else:
                result= chat(query)
            # 연산 결과를  템플릿으로 전달
            if result:
                # 사용자 및 챗봇 메시지를 대화 기록에 추가
                conversation_history = request.session.get('conversation_history', [])
                conversation_history.append({'user': query, 'chatbot': result})
                request.session['conversation_history'] = conversation_history
            #conversation_history = request.session.get('conversation_history', [])
            #return render(request, 'index.html', {'form': form, 'conversation_history': conversation_history})
    else:
        request.session['conversation_history'] = []
    conversation_history = request.session.get('conversation_history', [])

    # GET 요청이거나 폼이 유효하지 않은 경우
    return render(request, 'gptans.html', {'form': form, 'conversation_history': conversation_history})


chat_dic = {}
row = 0
for rule in chatbot_data['rule']:
    chat_dic[row] = rule.split('|')
    row += 1

def chat(request):
    candidate_responses = []

    for k, v in chat_dic.items():
        index = -1
        for word in v:
            try:
                if index == -1:
                    index = request.index(word)
                else:
                    # 이전 index 값은 현재 index값보다 이전이어야 한다.
                    if index < request.index(word, index):
                        index = request.index(word, index)
                    else:   # index 값이 이상할 경우 과감하게 break를 한다
                        index = -1
                        break
            except ValueError:
                index = -1
                break
        if index > -1:
            candidate_responses.append(chatbot_data['response'][k])

    # 후보 응답 중에서 무작위로 하나를 선택하여 반환합니다.
    if candidate_responses:
        return random.choice(candidate_responses)
    else:
        return '무슨 말인지 모르겠어요'

def event(data, ev_type):
    # 빈 리스트 초기화
    event_list = []

    # cu_data의 첫 번째 열이 ev_type과 일치하는 행 찾기
    matching_rows = data[data.iloc[:, 0] == ev_type]

    for index, row in matching_rows.iterrows():
        for item in row[1:2]:
            if isinstance(item, str) and ')' in item:
                event_list.append(item.split(')')[1])
            else:
                # ')'가 없거나 int인 경우 전체 값을 추가
                event_list.append(item)

    # 결과 리스트 출력
    return event_list[:10]