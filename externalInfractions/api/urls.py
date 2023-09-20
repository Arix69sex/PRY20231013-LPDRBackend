# your_app/urls.py

from django.urls import path
from externalInfractions.api.views.createMockInfraction import createMockInfraction
from externalInfractions.api.views.getMockInfractions import getMockInfractions
from externalInfractions.api.views.getMockInfractionsByCode import getMockInfractionsByCode

urlpatterns = [
    path('', getMockInfractions, name='get All Mocked External Infractions'),
    path('code/<str:code>', getMockInfractionsByCode, name='get All Mocked External Infractions'),
    path('create', createMockInfraction, name='Create a Mocked Infraction of an External Service')
]