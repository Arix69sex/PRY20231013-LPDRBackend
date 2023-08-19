# your_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers, name='get All Users'),
    path('', views.createUser, name='Create an User'),
    #path('<int:userId>', views.getUsersById, name='get User By Id'),  
    #path('<int:userId>', views.createUser, name='Update an User'),
    #path('<int:userId>', views.createUser, name='Delete an User'),
]