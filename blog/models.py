from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32,default='Title')
    content = models.TextField(null=True)
    def __str__(self):
        #list_display = ('id', 'title', 'content')
        return self.title