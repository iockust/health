from dashborad.api.views import (apiOverview, healthList, healthPatients, healthPatientHeartRatePerMinutePerDay)

from django.urls import path

urlpatterns = [
    path('', apiOverview, name='api-overview'),
    path('health-list/<int:pk>/', healthList, name='health-list'),
    path('health-patients/', healthPatients, name='patients'),
    path('health-PatientHeartRatePerMinutePerDay/<int:pk>/', healthPatientHeartRatePerMinutePerDay
         , name='health-PatientHeartRatePerMinutePerDay')
]
