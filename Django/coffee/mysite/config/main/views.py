from django.shortcuts import render
from django.http import HttpResponse #페이지 요청에 대한 응답을 할 수 있도록 해주는 함수
# Create your views here.


def index(request):
    """
    A view that displays the index page,


    """
    return render(request, 'main/index_a.html')


def colrom(request):
     return render(request, 'main/Colombia_a.html')

def brazil(request):
     return render(request, 'main/Brazil_a.html')

def ethiopia(request):
     return render(request, 'main/Ethiopia_a.html')

def kenya(request):
     return render(request, 'main/Kenya_a.html')



   


