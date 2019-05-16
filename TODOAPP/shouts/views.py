from django.shortcuts import render, redirect
from .models import Shout
from .forms import ShoutForm, ShoutModelForm

# Create your views here.
def home(request):
    if request.method=='POST':
        # 글 작성
        Shout.objects.create(
            content = request.POST.get('content'),
            title = request.POST.get('title')
        )
        return redirect('shouts:home')
    else:
        shouts = Shout.objects.all()
        return render(request, 'shouts/home.html', {'shouts':shouts})
        
def create(request):
    #Django가 만들어주는 form을 활용해서 글 작성을 한다.
    if request.method == 'POST':
        # (1). form class 사용
        # DB에 저장
        # 1. DB 유효성 검증
        # form = ShoutForm(request.POST)
        # if form.is_valid():
        #     title = form.cleaned_data.get('title')
        #     content = form.cleaned_data.get('content')
        #     Shout.objects.create(title=title, content=content)
        # return redirect('shouts:home')
        
        # (2). model Form class 사용
        form = ShoutModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('shouts:home')
        
    else:
        # form을 보여주는 페이지
        form = ShoutModelForm()
        return render(request, 'shouts/create.html', {'form':form})
        
def update(request, id):
    shout= Shout.objects.get(pk=id)
    if request.method=="POST":
        form = ShoutModelForm(request.POST, instance=shout)
        if form.is_valid():
            form.save()
        return redirect('shouts:home')
    else:
        form = ShoutModelForm(instance = shout)
        return render(request, 'shouts/update.html', {'form':form})