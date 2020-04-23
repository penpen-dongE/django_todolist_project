from django.shortcuts import render
# from django.http import HttpResponse
from .models import Todo
from .forms import AddForm
from django.shortcuts import redirect


# Create your views here.

def todo_view(request):
    if request.method == 'POST':        # Request == POST??
        form = AddForm(request.POST)    # AddForm의 인스턴스(객체) 생성
        if form.is_valid():     # Form의 형식이 유효한지 확인
            form.save()         # Form 저장 후 DB에 추가

    todos = Todo.objects.all()
    form = AddForm()
    data = {
        "todos": todos,
        "form": form,
    }

    return render(request, "todo_list.html", data)


def todo_progress_view(request):
    todos = Todo.objects.exclude(is_done=True)
    data = {
        "todos": todos,
    }

    return render(request, "todo_in_progress.html", data)


def delete_todo(request, pk):   # pk는 각 DB 튜플의 고유번호
    target = Todo.objects.get(pk=pk)    # Model에서 삭제하려는 튜플을 불러오기
    target.delete()             # 해당 튜플을 제거
    return redirect("todos")    # name='todos' 주소로 돌아감
