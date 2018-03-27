from django.urls import path,include

from . import views
#app_name = 'blog'  #引入 命名空间 配置超链接的url 会用到

urlpatterns = [
    path('', views.index),
]
