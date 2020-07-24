from rest_framework import serializers
from backend.models import Health, Patient, HourlyHeartRate, WeeklyHealthSummary


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
        model = Health
        fields = '__all__'
        model = HourlyHeartRate
        fields = ['Hour', 'HeartRate']

class PatientTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Health
        fields=['time']

class WeeklyHealthSummarySerializer(serializers.ModelSerializer):
    averagesleep=serializers.ReadOnlyField()
    class Meta:
        model=Health
        fields=['averagesleep']