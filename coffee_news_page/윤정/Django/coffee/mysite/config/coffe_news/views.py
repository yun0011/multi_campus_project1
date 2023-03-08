from django.shortcuts import render
from django.http import HttpResponse #페이지 요청에 대한 응답을 할 수 있도록 해주는 함수
from .models import CsvTable2
# Create your views here.


def index(request):
    """
    A view that displays the index page,
    """
    news_list = CsvTable2.objects.all()
    context = {'news_list': news_list}
    return render(request, 'coffe_news/index.html', context)
   

