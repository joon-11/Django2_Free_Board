from .forms import CustomUserCreationForm
from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'main/index.html')


def blog(request):
    # 모든 Post를 가져와 postlist에 저장
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옴
    return render(request, 'main/blog.html', {'postlist':postlist})


def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post})


def new_post(request):
    if request.method == 'POST':
        new_article = Post.objects.create(
            postname=request.POST['postname'],
            contents=request.POST['contents'],
        )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})

# myapp/views.py


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/blog/')  # 회원가입 성공 후 로그인 페이지로 리다이렉트
    else:
        form = CustomUserCreationForm()

    return render(request, 'main/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인 성공 시
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/blog/')  # 로그인 성공 후 리다이렉트
        else:
            # 로그인 실패 시
            # form 에러 처리 또는 원하는 예외 처리를 수행합니다.
            pass
    else:
        form = AuthenticationForm()

    return render(request, 'main/login.html', {'form': form})