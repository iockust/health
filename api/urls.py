from .views import (apiOverview, healthList, healthPatients, healthPatientHeartRatePerMinutePerDay,
                                 healthPatientHeartRatePerHourPerDay,weeklyHealthSummary,dailyHealthSummary)

from django.urls import path

urlpatterns = [
    path('', apiOverview, name='api-overview'),
    path('health-list/<int:pk>/', healthList, name='health-list'),
    path('health-patients/', healthPatients, name='patients'),
    path('health-PatientHeartRatePerMinutePerDay/<int:pk>/', healthPatientHeartRatePerMinutePerDay, name='health-PatientHeartRatePerMinutePerDay'),
    path('health-PatientHeartRatePerHourPerDay/<int:pk>/', healthPatientHeartRatePerHourPerDay, name='health-PatientHeartRatePerHourPerDay'),
    path('weekly-health-Summary/<int:pk>/',weeklyHealthSummary, name='health-summary'),
    path('daily-health-summary/',dailyHealthSummary,name='daily-health-summary'),
    
]
