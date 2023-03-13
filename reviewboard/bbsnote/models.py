from django.db import models

# Create your models here.
class Board(models.Model): # 게시글 모델
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Comment(models.Model): #댓글 모델
    Board = models.ForeignKey(Board, on_delete=models.CASCADE) #보드에 있는 글이 없어지면 같이 지워
    content = models.TextField()
    create_date = models.DateTimeField()