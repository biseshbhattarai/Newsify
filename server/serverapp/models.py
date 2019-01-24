from django.db import models


#TODO
class Image(models.Model):
    name = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    photo = models.FileField(upload_to="media")

    def __str__(self):
        return self.name + ':' + self.category 


class News(models.Model):
    trending = models.BooleanField(default=False)
    title = models.CharField(max_length=120)
    summary = models.CharField(max_length=120)
    full_news = models.CharField(max_length=200000000000, null=True)
    like = models.IntegerField(default=0)


    def __int__ (self):
        return self.pk



