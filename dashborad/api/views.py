from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from dashborad.models import Health, Patient, HourlyHeartRate
from dashborad.api.serializer import HeartRateSerializer, PatientSerializer, HealthSerializer, HourlyHeartRateSerializer,HealthSummarySerializer
from dashborad.api.filters import HealthFilter


import datetime
import time
from django.utils.dateparse import parse_date
from django.db.models import Avg, Max, Min, Sum
from datetime import datetime, date, time, timedelta

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/health-list/<int:pk>/',
        'PatientsList': 'health-patients/',
        'Health-PatientHeartRatePerMinutePerDay': 'health-PatientHeartRatePerMinutePerDay/<int:pk>/',
        'Health-PatientHeartRatePerHourPerDay': 'health-PatientHeartRatePerHourPerDay/<int:pk>/',
        'health-Summary':'health-Summary/<int:pk>'
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


# @api_view(['GET'])
# def  healthHeartRate(request,pk,date):
#     if request.method=='GET':
#         startdate=request.data.get('startdate')
#         enddate=request.data.get('enddate')
        
#         # filter_data = HealthFilter(request.GET, queryset=Health.objects.all())
#         # filter_data=Health.objects.filter(date__range=[startdate, enddate])
#         filter_data=Health.objects.filter(id=pk).filter(time_gte=startdate).filter(time_lte=enddate)
#         serializer=HealthFilterSerializer(filter_data,many=True)
#         return Response(serializer.data)
#     # except Patient.date_error_message

# @api_view(['GET'])
# def  healthHeartRate(request):
#     pk = request.query_params.get('id')
#     str_date = request.query_params.get('strDate')
#     start_date = datetime.datetime.strptime(str_date, '%Y-%m-%d').date()

#     end_date = start_date + datetime.timedelta(days=1)
#     filter_date = Health.objects.filter(
#         pk=pk,
#         time__gte=start_date,
#         time__lte=end_date
#     )
#     serializer=HealthFilterSerializer(filter_date,many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def healthHeartRate(request):
#     if request.method == 'GET':
#         date_input = request.query_params.get('strDate', None)
#         pk = request.query_params.get('id')
#         health_qs = Health.objects.filter(pk=pk, time__date=date_input)
#         serializer = HealthFilterSerializer(health_qs, many=True)
#         return Response(serializer.data)
# =======
@api_view(['GET'])
def healthPatientHeartRatePerHourPerDay(request, pk):
    if request.method == 'GET':
        strDate = request.query_params.get('strDate', None)
        startDate = parse_date(strDate)
        endDate = startDate + datetime.timedelta(days=1)

        hourlyrate = HourlyHeartRate.objects.hourly_avg_rate(pk, startDate, endDate)

        serializer = HourlyHeartRateSerializer(hourlyrate, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def healthSummary(request,pk):
    if request.method == 'GET':
        strDate = request.query_params.get('strDate', None)
        # date_str = parse_date(strDate)
        # date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        date_obj= parse_date(strDate)
        start_of_week = date_obj - timedelta(days=date_obj.weekday())  # Monday
        end_of_week = start_of_week + timedelta(days=6)  # Sunday

        # weekly_avg_hearrate = Health.objects.filter(time__lte=end_of_week,time__gt=start_of_week.timedelta(days=7)).values('value').aggregate(Avg('value'))
        # all_data=Health.objects.all()
        weekly_avg_hearrate=Health.objects.filter(time__lte=start_of_week - timedelta(days=7),time__lt=start_of_week).aggregate(average_price=Avg('value'))
        serializer=HealthSummarySerializer(all_data,many=True)
        return Response(serializer.data)




