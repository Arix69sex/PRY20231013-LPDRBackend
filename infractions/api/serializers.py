from rest_framework import serializers
from infractions.api.models import Infraction

class InfractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraction
        fields = ('id', 'infractionCode', 'ballotNumber', 'name', 'level', 'fine', 'licensePlate', 'date')

