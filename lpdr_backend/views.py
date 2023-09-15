# main_app/api/views.py

from rest_framework import generics
from users.api.serializers import UserSerializer
from users.api.models import User

class MyAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer