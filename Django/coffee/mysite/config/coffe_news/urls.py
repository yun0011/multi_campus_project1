from django.urls import path

import coffe_news.views as views

urlpatterns = [
    path('', views.index, name='index'),
    ]
