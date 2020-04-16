from django.db import models

# Create your models here.

# Todo 클래스는 models.Model을 상속 받는다.
# 상속을 받는다는 것의 핵심? - 상속 받는 자는 상속 하는 자의 변수, 함수 등을 가져다 쓸 수 있음!

# 할 일의 내용은 문자형, 할 일의 여부는 논리형으로 한다.


class Todo(models.Model):
    task = models.CharField(max_length=200, null=False,
                            help_text=" 할 일을 채워주세요!")
    is_done = models.BooleanField(default=False)
