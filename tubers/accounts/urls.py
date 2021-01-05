from django.urls import path 
from . import views

urlpatterns = [
    path('login', views.login,name="login"),
    path('register',views.register, name="register"),
    path('logout',views.logout_user, name='logout'), #logout_user is inbuilt feature of django,so is called as logout_user
    path('dashboard',views.dashboard, name='dashboard'),
]
