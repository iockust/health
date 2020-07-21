from django.urls import path, include
from .views import MainPageView,ContactPageView

urlpatterns = [

    path('', MainPageView.as_view(), name='dashborad-main'),
    path('contact',ContactPageView.as_view(),name='dashborad-contact'),
]
