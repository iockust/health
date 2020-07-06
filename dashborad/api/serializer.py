from rest_framework import serializers
from dashborad.models import Health

class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model=Health
        fields='__all__'
 