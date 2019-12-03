from django.urls import path
from comment import views

app_name = 'comment'

urlpatterns = [
    path('comment/<int:article_id>/', views.comment_post, name='comment_post'),
]