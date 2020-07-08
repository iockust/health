# from rest_framework import serializers
# from dashborad.models import Health, Patient, HourlyHeartRate,WeeklyHealthSummary


# class HealthSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Health
#         fields = '__all__'


# class PatientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Patient
#         fields = '__all__'


# class HeartRateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Health
#         fields = ['time', 'value']


# class HourlyHeartRateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Health
#         # fields=['time','value']
#         fields= '__all__'
#         model = HourlyHeartRate
#         fields = ['Hour', 'HeartRate']


# class HourlyHeartRateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Health
#         # fields=['time','value']
#         fields= '__all__'
#         model = HourlyHeartRate
#         fields = ['Hour', 'HeartRate']


# class HealthSummarySerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Health
#         fields ='__all__'
#         model=WeeklyHealthSummary
#         fields=['value','intensity','sleepminute']


