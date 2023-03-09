from django.shortcuts import render
from django.http import HttpResponse #페이지 요청에 대한 응답을 할 수 있도록 해주는 함수
from .models import CsvTable2
# Create your views here.
from django.core.paginator import Paginator


def index(request):
    """
    A view that displays the index page,


    """
#####################################페이징 처리
    news_list = CsvTable2.objects.all()
    page = request.GET.get('page', '1') # 페이지

    paginator = Paginator(news_list, 10) # Show 10 contacts per page.
    page_object = paginator.get_page(page)

    # news_list = CsvTable2.objects.all()
    context = {'news_list':page_object }
    return render(request, 'coffe_news/index.html', context)

   



   

