from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def home(request):
    if request.method == "POST":
        # Todo 작성하기
        # 1. Todo form을 통해 전달된 데이터를 데이터 베이스에 저장
        Todo.objects.create(
            content=request.POST.get('content'),
            user = request.user
        )
        # 2. redirect
        return redirect('todos:home')
    else:
        return render(request, 'todos/home.html')

def check(request, id):
    # Todo의 completed 칼럼의 값을 변경한다
    # 1. Todo 테이블에서 변경하고자 하는 레코드를 찾아온다.
    # 2. 찾아온 레코드의 값을 변경한다
    todo = Todo.objects.get(pk=id)
    todo.completed = True if not todo.completed else False
    todo.save()
    return redirect('todos:home')
    
def delete(request,id):
    todo = Todo.objects.get(pk=id)
    todo.delete()
    return redirect('todos:home')

def update(request, id):
    todo = Todo.objects.get(pk=id)
    if request.method == "GET":
        return render(request, 'todos/update.html', {'todo': todo})
    else:
        todo.content = request.POST.get('content')
        todo.save()
        return redirect('todos:home')