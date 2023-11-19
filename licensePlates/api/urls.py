# your_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getLicensePlates, name='get All License Plates'),
    path('create', views.createLicensePlate, name='Create a License Plate'),
    path('user/<int:userId>', views.getLicensePlateByUserId, name='get License Plate By User Id'),  
    path('<int:licensePlateId>', views.getLicensePlateById, name='get License Plate By Id'),  
    path('<int:licensePlateId>/update', views.updateLicensePlate, name='Update a License Plate'),
    path('detect', views.detectLicensePlateWithInfractions, name='Detect License Plate With Infractions'),
    path('image/<int:licensePlateId>', views.getImageOfLicensePlate, name='Get Image Of License Plate'),
    path('validate', views.validateFunctionality, name='Validate functionality')
]