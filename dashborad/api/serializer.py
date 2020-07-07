from rest_framework import serializers
from dashborad.models import Health, Patient, HourlyHeartRate


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class HeartRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = ['time', 'value']


class HourlyHeartRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HourlyHeartRate
        fields = ['Hour', 'HeartRate']
