# your_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers, name='get All Users'),
    path('create', views.createUser, name='Create an User'),
    path('<int:userId>', views.getUsersById, name='get User By Id'),  
    path('<int:userId>/update', views.updateUser, name='Update an User'),
    path('<int:userId>/delete', views.deleteUser, name='Delete an User'),
    path('login', views.login, name='Login'),
    path('signup', views.signUp, name='SignUp'),
]