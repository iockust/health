from django.views.generic import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse
# from .models import Health, Patient
from django.core import serializers


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        patients = Patient.objects.all()
        return render(request, 'dashborad/main.html', {'patients': patients})


class ChartsPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashborad/charts.html')


class ChartsData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "labels": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "data": [12, 19, 3, 5, 2, 3, 10],
        }

        return Response(data)
