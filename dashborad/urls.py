from django.urls import path,include
from .views import MainPageView,ChartsData,ChartsPageView,ReportPageView


urlpatterns = [

    path('',MainPageView.as_view(),name='dashborad-main'),
    path('charts/',ChartsPageView.as_view(),name='dashborad-charts'),
    path('api/charts/data/', ChartsData.as_view(),name='dashborad-charts-api'),

    # REST FRAMEWORK URLS
    path('api/',include('dashborad.api.urls')),

]