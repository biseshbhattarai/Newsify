from django.db import models


#TODO
class Image(models.Model):
    name = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    photo = models.FileField(upload_to="media")

    def __str__(self):
        return self.name + ':' + self.category 

class Category(models.Model):
    news_pk = models.IntegerField(default=0)
    topics = models.CharField(max_length=50)

    def __str__(self):
        return self.topics

class News(models.Model):
    trending = models.BooleanField(default=False)
    title = models.CharField(max_length=120)
    summary = models.CharField(max_length=120, null=True)
    like = models.IntegerField(default=0)
    full_url = models.CharField(max_length=100, null=True)
    publishedDate = models.DateTimeField(null=True)
    author = models.CharField(max_length=50, null=True)
    sentiment = models.CharField(max_length=50, null=True)


    def __str__ (self):
        return 'Hello'


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __int__(self):
        return self.pk