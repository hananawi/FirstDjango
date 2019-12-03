from django.urls import path
from article import views

app_name = 'article'

urlpatterns = [
    path('<str:username>/article_modify/<int:article_id>/', views.article_modify, name='article_modify'),
    path('<str:username>/article_post/', views.article_post, name='article_post'),
    path('article_detail/<int:article_id>/', views.article_detail, name='article_detail'),
    path('<int:user_id>/article_delete/<int:article_id>/', views.article_delete, name='article_delete'),
]
