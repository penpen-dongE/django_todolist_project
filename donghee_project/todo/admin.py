from django.contrib import admin
from .models import Todo
# Register your models here.

# admin.site.Register를 통해 관리자 페이지에 Model을 등록

admin.site.register(Todo)
