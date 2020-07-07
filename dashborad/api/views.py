from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from dashborad.models import Health, Patient
from dashborad.api.serializer import HeartRateSerializer, PatientSerializer, HealthSerializer
from dashborad.api.filters import HealthFilter
from django.utils.dateparse import parse_date
import datetime


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/health-list/<int:pk>/',
        'PatientsList': 'health-patients/',
        'Health-PatientHeartRatePerMinutePerDay': 'health-PatientHeartRatePerMinutePerDay/<int:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def healthList(request, pk):
    try:
        # health=Health.objects.get(slug=slug)
        strDate = request.query_params.get('strDate', None)
        startDate = parse_date(strDate)
        endDate = startDate + datetime.timedelta(days=1)

        health = Health.objects.filter(id=pk).filter(time__gte=startDate).filter(time__lte=endDate)


    except Health.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = HealthSerializer(health, many=True)
        return Response(serializer.data)


# Jawad
@api_view(['GET'])
def healthPatients(request):
    try:

        patients = Patient.objects.all()

    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)


# if state_name is not None:
# queryset = queryset.filter(state__name=state_name)
@api_view(['GET'])
def healthPatientHeartRatePerMinutePerDay(request, pk):
    if request.method == 'GET':
        strDate = request.query_params.get('strDate', None)
        startDate = parse_date(strDate)
        endDate = startDate + datetime.timedelta(days=1)

        health = Health.objects.filter(id=pk).filter(time__gte=startDate).filter(time__lte=endDate)

        serializer = HeartRateSerializer(health, many=True)
        return Response(serializer.data)
    # except Patient.date_error_message
