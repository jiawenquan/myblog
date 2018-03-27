from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    #显示用户管理
    list_display = ('id','title','content')


admin.site.register(Article,ArticleAdmin)   #配置Article 管理

