from rest_framework import serializers
from externalInfractions.api.models import ExternalInfraction

class ExternalInfractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalInfraction 
        fields = ('id', 'code', 'name', 'level', 'fine')