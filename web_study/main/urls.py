from django.contrib import admin
from django.urls import path
from .views import index, blog, posting, new_post, remove_post, signup, user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_login, name='login'),  # 시작 페이지를 로그인 페이지로 설정합니다.
    path('index/', index, name='index'),  # 예를 들어, 로그인 후 리디렉션할 페이지를 지정할 수 있습니다.
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>/', posting, name="posting"),
    path('blog/new_post/', new_post),
    path('blog/<int:pk>/remove/', remove_post),
    path('signup/', signup, name='signup'),
]
