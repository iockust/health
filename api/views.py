import pytz
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import sys
sys.path.append("..")

from  backend.models import Health, Patient, HourlyHeartRate, WeeklyHealthSummary, MinuteHeartRate
from  backend.serializer import (HeartRateSerializer, PatientSerializer, HealthSerializer, HourlyHeartRateSerializer,PatientTimeSerializer,WeeklyHealthSummarySerializer)

from django.core import serializers
from django.utils.dateparse import parse_date
from django.db.models import Avg, Max, Min, Sum,F
from datetime import datetime, date, time, timedelta
from django.db.models import Max,Min,Avg,F
from django.http import JsonResponse
from django.db import connections
import json
from django.core.serializers.json import DjangoJSONEncoder




@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/health-list/<int:pk>/',
        'PatientsList': 'health-patients/',
        'Health-PatientHeartRatePerMinutePerDay': 'health-PatientHeartRatePerMinutePerDay/<int:pk>/',
        'Health-PatientHeartRatePerHourPerDay': 'health-PatientHeartRatePerHourPerDay/<int:pk>/',
        'weekly-health-Summary':'weekly-health-Summary/<int:pk>',
        'Actvities of Patient':'healthPatientActivities/'

    }

    return Response(api_urls)


@api_view(['GET'])
def healthList(request, pk):
    try:
        # health=Health.objects.get(slug=slug)
        strDate = request.query_params.get('strDate', None)
        startDate = parse_date(strDate)
        endDate = startDate + timedelta(days=1)

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


@api_view(['GET'])
def healthPatientHeartRatePerMinutePerDay(request, pk):
    if request.method == 'GET':
        strDate = request.query_params.get('strDate', None)
        startDate = parse_date(strDate)
        # startDate = parse_date(strDate + " 00:00:00")
        # startDate = datetime.strptime(strDate + " 00:00:00", '%Y-%m-%d %H:%M:%S')
        # aware_StartDate = pytz.timezone('US/Eastern').localize(startDate, is_dst=None)
        # startDate = aware_StartDate.replace(tzinfo=None)
        endDate = startDate + timedelta(days=1)

        # health = Health.objects.filter(id=pk).filter(time__gte=aware_StartDate).filter(time__lte=endDate)
        #
        # serializer = HeartRateSerializer(health, many=True)

        heartrate = MinuteHeartRate.objects.get_heart_rate(pk, startDate, endDate)

        serializer = HeartRateSerializer(heartrate, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def healthPatientHeartRatePerHourPerDay(request, pk):
    if request.method == 'GET':
        strDate = request.query_params.get('strDate', None)
        startDate = parse_date(strDate)
        endDate = startDate + timedelta(days=1)

        hourlyrate = HourlyHeartRate.objects.hourly_avg_rate(pk, startDate, endDate)

        serializer = HourlyHeartRateSerializer(hourlyrate, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def weeklyHealthSummary(request, pk):
    if request.method == 'GET':
        strDate = request.query_params.get('strDate', None)
        date_obj= parse_date(strDate)

        # startdate= date_obj - timedelta(days=date_obj.weekday())  # Monday
        startdate=date_obj
        enddate= startdate + timedelta(days=6)  # Sunday 6
        stringstartdate='{}'.format(startdate)
        stringenddate='{}'.format(enddate)
        queryset=Health.objects.values('value','sleepminute').filter(time__gte=stringstartdate,time__lte=stringenddate).aggregate(Max('value'),Min('value'),Avg('value'))
        averageSleepQuery="SELECT DATE_FORMAT(SEC_TO_TIME(AVG(TIME_TO_SEC(SleepMinute))),'%H:%i:%s'),DATE_FORMAT(SEC_TO_TIME(AVG(TIME_TO_SEC(IntensityTime))),'%H:%i:%s') FROM dashborad_health where id='{}' and Time>= '{}' and Time< '{}'".format(pk,startdate,enddate)
        json_data = []
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute(averageSleepQuery)
            objs = cursor.fetchall() 
            for obj in objs:
                json_data.append({"AverageSleep":obj[0],"AverageIntensity":obj[1]})
        queryset.update(json_data[0])
        return JsonResponse(queryset, safe=False)



# @api_view(['GET'])
# def weeklyHealthSummary(request, pk):
#     if request.method == 'GET':
#         json_data = []
#         strDate = request.query_params.get('strDate', None)
#         from django.db import connection

#         date_obj= parse_date(strDate)

#         startdate= date_obj - timedelta(days=date_obj.weekday())  # Monday
#         enddate= start_of_week + timedelta(days=6)  # Sunday 6
        
#         with connection.cursor() as cursor:
    #             cursor.execute(""" SELECT avg(value) HeartRate, AVG(Intensity) Intensity,AVG(SleepValue) AS Sleep 
    #             ,Min(value) as MinHeartReate,Max(value) as MaxHearRate
#             FROM `dashborad_health`  where Id=%s and (Time BETWEEN %s AND %s ) """, (pid, startdate, enddate))
#             objs = cursor.fetchall()
#             for obj in objs:
#                 json_data.append({"AverageHeartReate" : obj[0], "Average" : obj[1],"Sleep":obj[2],"WalkTime":obj[3],"CaloriesBurnTime":obj[4],"EngeryExpendTime":obj[5],"Activity":obj[6],"WorkoutTime":obj[7],"CaloriesConsumed":obj[8]})
#         return JsonResponse(json_data, safe=False)


@api_view(['GET'])
def healthPatientActivities(request, pk):
    if request.method == 'GET':
        json_data = []
        strDate = request.query_params.get('strDate', None)
        startDate = parse_date(strDate)
        endDate = startDate + timedelta(days=1)
        query="SELECT id as PatientId ,DATE(Time) AS date,avg(value) AS AverageHeartRate,minute(SleepMinute) as Sleep,minute(StepsMinute)  as WalkTime,minute(CalMinute)  as CaloriesBurnTime,minute(MetMinute) as EngeryExpendTime,IF(Mets < 3, '25', IF(Mets>6,'70',IF((Mets<=3 and MEts <=6),'45',''))) as Activity,minute(IntensityTime) as WorkoutTime,Calories as CaloriesConsumed FROM dashborad_health where id={} and Time>= '{}' and Time< '{}' GROUP BY date order by date asc".format(pk,startDate,endDate)
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute(query)
            objs = cursor.fetchall()    
            for obj in objs:
                json_data.append({"id" : obj[0],"date":obj[1], "AverageHeartRate" : obj[2],"Sleep":obj[3],"WalkTime":obj[4],"CaloriesBurnTime":obj[5],"EngeryExpendTime":obj[6],"Activity":obj[7],"WorkoutTime":obj[8],"CaloriesConsumed":obj[9]})
        return JsonResponse(json_data, safe=False)

@api_view(['GET'])
def healthPatientActivitiesDate(request, pk):
    if request.method == 'GET':
        json_data=[]
        data=Health.objects.values('time').filter(id=pk)     
        q="SELECT distinct DATE_FORMAT(Time, '%Y %m %d') as Date FROM iockustc_health.dashborad_health where id='{}'".format(pk)
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute(q) 
            objs=cursor.fetchall()
            for obj in objs:
                json_data.append({"Date":obj[0]})
        print(json_data)
        # print(data)
        # serializer = PatientTimeSerializer(data,many=True)
  
        # return JsonResponse(serializer.data,safe=False)
        return JsonResponse(json_data,safe=False)

# SELECT DATE(Time) AS date,
#  avg(value) AS AverageHeartRate,
#  DATE_FORMAT(SleepMinute,'%H:%i') as Sleep,
#  DATE_FORMAT(StepsMinute,'%H:%i')  as WalkTime,
#  DATE_FORMAT(CalMinute,'%H:%i')  as CaloriesBurnTime,
#  DATE_FORMAT(MetMinute,'%H:%i')  as EngeryExpendTime,IF(Mets < 3, 'Light Activity', IF(Mets>6,'Vigorous Activity',IF((Mets<=3 and MEts <=6),'Moderate Activity',''))) as Activity,DATE_FORMAT(IntensityTime,'%H:%i') as WorkoutTime,
# Calories as CaloriesConsumed 
# FROM dashborad_health  where id=5577150313 and Time>= '2016-04-6' and Time< '2016-04-10' GROUP BY date order by date asc
