from django.db import models


class Urls(models.Model):
    url = models.URLField()
    number = models.IntegerField(null=True)
    def __str__(self):
        return self.url
    def __int__(self,url,number):
        super.__init__()
        self.url = url
        self.number = number

    # def __init__(self):
    #     super.__init__()
# Create your models here.
