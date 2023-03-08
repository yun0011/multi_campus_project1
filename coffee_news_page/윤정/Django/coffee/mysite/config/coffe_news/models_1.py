from django.db import models

# Create your models here.

class Article(models.Model):
    date = models.DateTimeField()
    subject = models.CharField(max_length = 300)
    content = models.TextField()
    link = models.URLField()

class Answer(models.Model):
    ##질문에 대한 답변이므로 질문을 속성으로 가져아야한다.
    # cascade는 질문이 삭제되면 답변도 삭제되도록 하는 옵션
    # ForeignKey는 다른 모델과 연결할 때 사용하는 필드
    content = models.TextField()
    create_date = models.DateTimeField()
    