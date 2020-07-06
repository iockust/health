from dashborad.api.views import (apiOverview, healthList,healthDetial,
healthCreate,healthUpdate,healthDelete,healthDateFilter)

from django.urls import path


urlpatterns=[
    path('',apiOverview,name='api-overview'),
    path('health-list/',healthList,name='health-list'),
    path('health-detail/<str:pk>/',healthDetial,name='health-detail'),
    path('health-create/',healthCreate,name='health-create'),
    path('health-update/<str:pk>/',healthUpdate,name='health-update'),
    path('health-delete/<str:pk>/',healthDelete,name='health-Delete'),
    path('health-date/',healthDateFilter,name='health-datefilter'),

]

