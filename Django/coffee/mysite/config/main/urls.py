from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('Colombia_a.html/', views.colrom),
    path('Brazil_a.html/', views.brazil),
    path('Ethiopia_a.html/', views.ethiopia),  
    path('Kenya_a.html/', views.kenya),  

]