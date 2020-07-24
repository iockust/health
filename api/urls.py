from .views import (apiOverview, healthList, healthPatients, healthPatientHeartRatePerMinutePerDay,
                                 healthPatientHeartRatePerHourPerDay,weeklyHealthSummary,healthPatientActivities,healthPatientActivitiesDate)

from django.urls import path

urlpatterns = [
    path('', apiOverview, name='api-overview'),
    path('health-list/<int:pk>/', healthList, name='health-list'),
    path('health-patients/', healthPatients, name='patients'),
    path('health-PatientHeartRatePerMinutePerDay/<int:pk>/', healthPatientHeartRatePerMinutePerDay, name='health-PatientHeartRatePerMinutePerDay'),
    path('health-PatientHeartRatePerHourPerDay/<int:pk>/', healthPatientHeartRatePerHourPerDay, name='health-PatientHeartRatePerHourPerDay'),
    path('weekly-health-Summary/<int:pk>/',weeklyHealthSummary, name='health-summary'),
    path('health-patient-activites/<int:pk>/',healthPatientActivities,name='health-patient-activities'),
    path('health-patient-activites-date/<int:pk>/',healthPatientActivitiesDate,name='health-patient-activities-date')

]
