from django.db import models

# Create your models here.


# django 모델 만들기
# models. Model 을 상속
#
class Photo(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    describe = models.TextField()
    price = models.IntegerField()

