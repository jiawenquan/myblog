from django.urls import path,include

from . import views

#app_name = 'blog'  #引入 命名空间 配置超链接的url 会用到
urlpatterns = [
    path('', views.index),
    path('article/<int:article_id>', views.article_page,name='article_page'),          #2.0版本指定id
    path('edit/<int:article_id>',views.edit_page,name='edit_page'),
    path('edit/action', views.edit_action, name='edit_action'),
]
