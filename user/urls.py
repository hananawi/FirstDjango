from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('homepage/', views.homepage, name='homepage'),
    path('logout/', views.user_logout, name='logout'),
    path('<str:username>/profile/', views.profile, name='profile'),
]
