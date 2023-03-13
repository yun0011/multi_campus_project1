"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # include는 다른 urlconf를 참조할 수 있도록 해줌
from coffe_news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coffe_news/', include('coffe_news.urls')),
    path('main/',include('main.urls')), 
    path('main/index.html', include('coffe_news.urls')),
    
                                                 
                                                    ##처음시작할때 보여줄 페이지인것임 -> views.py에 index함수를 만들어줘야함
]                                                     ##coffe_news/로 시작하는 모든 url은 coffe_news.urls로 전달됨
                                                      ##앞으로 만들어질 모든 url은 coffe_news.urls로 전달됨
