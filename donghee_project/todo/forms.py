from django import forms
from .models import Todo

# AddForm이라는 클래스 안에 Meta라는 form을 하나 만들어줌
# 이렇게 만들어진 form은 views.py가 처리해준다.


class AddForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('task',)
