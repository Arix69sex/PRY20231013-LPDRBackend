# your_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getVehicles, name='get All Vehicles'),
    path('create', views.createVehicle, name='Create a Vehicle'),
    path('licensePlate/<int:licensePlateId>', views.getVehicleByLicensePlateId, name='get Vehicle By License Plate Id'),  
    path('<int:vehicleId>', views.getVehicleById, name='get Vehicle By Id'),  
    path('<int:vehicleId>/update', views.updateVehicle, name='Update a Vehicle')
]