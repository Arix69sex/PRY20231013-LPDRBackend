# your_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsersData, name='Get All Users Data'), 
    path('<int:userDataId>', views.getUserDataById, name='Get User Data by Id'),  
    path('<int:userId>/create', views.createUserData, name='Create User Data by User Id'),  
    path('<int:userId>/data', views.getUserDataByUserId, name='Get User Data by User Id'),
    path('<int:userDataId>/update', views.updateUserData, name='Update User Data by User Data Id'), 
]