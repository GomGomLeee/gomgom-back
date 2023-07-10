from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()
CHOICES = (
        ('대인관계','대인관계'),
        ('연애','연애'),
        ('교육','교육'),
        ('생활','생활'),
        ('건강','건강'),
        ('반려동물','반려동물'),
        ('여행','여행'),
        ('쇼핑','쇼핑'),
        ('기타','기타'),
)

class Post(models.Model):
    title = models.TextField(verbose_name='질문제목')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일',auto_now_add=True)
    view_count = models.IntegerField(verbose_name='조회수',blank=True, default = 0)
    heart_count = models.IntegerField(verbose_name='공감수',blank=True, default = 0)
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=20, choices=CHOICES,default='기타' )


class Comment(models.Model):
    image = models.ImageField(verbose_name = '이미지',null=True,blank = True)
    content= models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일',auto_now_add=True)
    post=models.ForeignKey(to='Post',on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)
    
class Selection(models.Model):
    image=models.ImageField(verbose_name = '이미지',null=True,blank = True)
    content = models.CharField(verbose_name='내용',max_length=100)
    vote = models.CharField(verbose_name = '투표율', default = "50%")
    post = models.ForeignKey(to='Post',on_delete=models.CASCADE,null=True,blank=True)