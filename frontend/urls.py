from django.urls import path, include
from .views import MainPageView,ContactPageView,ActivitesPageView

urlpatterns = [

    path('', MainPageView.as_view(), name='dashborad-main'),
    path('contact',ContactPageView.as_view(),name='dashborad-contact'),
    path('activities',ActivitesPageView.as_view(),name='dashborad-activities')
]
