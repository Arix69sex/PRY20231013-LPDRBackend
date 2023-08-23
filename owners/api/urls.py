# your_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getOwners, name='get All Owners'),
    path('create', views.createOwner, name='Create a Owner'),
    path('licensePlate/<int:licensePlateId>', views.getOwnerByLicensePlateId, name='get Owner By License Plate Id'),  
    path('<int:ownerId>', views.getOwnerById, name='get Owner By Id'),  
    path('<int:ownerId>/update', views.updateOwner, name='Update a Owner')
]