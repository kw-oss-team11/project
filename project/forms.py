from django import forms

class QueryForm(forms.Form):
    query = forms.CharField(label='질문을 입력하세요 ', max_length=300)