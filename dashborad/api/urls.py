from dashborad.api.views import (apiOverview, healthList, healthPatients, healthPatientHeartRatePerMinutePerDay,
                                 healthPatientHeartRatePerHourPerDay,healthSummary)

from django.urls import path

urlpatterns = [
    path('', apiOverview, name='api-overview'),
    path('health-list/<int:pk>/', healthList, name='health-list'),
    path('health-patients/', healthPatients, name='patients'),
    path('health-PatientHeartRatePerMinutePerDay/<int:pk>/', healthPatientHeartRatePerMinutePerDay
         , name='health-PatientHeartRatePerMinutePerDay'),
    path('health-PatientHeartRatePerHourPerDay/<int:pk>/', healthPatientHeartRatePerHourPerDay
         , name='health-PatientHeartRatePerHourPerDay'),
    # Health Summary
    path('health-Summary/<int:pk>/',healthSummary, name='health-summary')
]
