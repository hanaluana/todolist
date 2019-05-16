from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
# users/login 에 들어왔을 때
def login_user(request):
    if request.method=="GET":
        return render(request, 'users/login.html')
    else:
        # 로그인을 시키고 (User를 인증하고)
        # 1. request에 포함된 user 정보(username, password)가 DB에 있는지 확인하기, 정보가 일치하는지 확인
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 1. authenticate로 user를 검증한다 : db에 해당하는 username을 가진 유저가 있고, 해당 유저의 password가 입력된 값과 같은가?
        user = authenticate(request, username=username, password=password)
        
        # 2. user를 로그인시킨다.
        # (서버에 해당유저가 유효한 유저임을 저장해둔다.)
        if user:
            login(request, user)
            # 유저에게 성공적으로 로그인이 되었다고 알려준다.
            messages.success(request, '로그인에 성공했습니다')
            return redirect('todos:home')
        else:
            messages.success(request, '로그인에 실패하였습니다')
            return redirect('users:login')
            # 로그인이 안됬다고 알려준다.
        
def logout_user(request):
    # 세션에서 유저를 지운다.
    logout(request)
    messages.success(request, '성공적으로 로그아웃 되었습니다')
    return redirect('todos:home')


def profile(request):
    return render(request, 'users/profile.html')
    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.instance)
            messages.success(request, '환영합니다! '+form.instance.username+'님')
            return redirect('todos:home')
        else:
            messages.success(request, '회원가입에 실패하였습니다')
            return redirect('users:register')
    else:
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form':form})