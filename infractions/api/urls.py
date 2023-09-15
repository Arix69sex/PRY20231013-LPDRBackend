# your_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getInfractions, name='get All Infractions'),
    path('create', views.createInfraction, name='Create a Infraction'),
    path('licensePlate/<int:licensePlateId>', views.getInfractionByLicensePlateId, name='get Infraction By License Plate Id'),  
    path('<int:infractionId>', views.getInfractionById, name='get Infraction By Id'),  
    path('<int:infractionId>/update', views.updateInfraction, name='Update an Infraction')
]