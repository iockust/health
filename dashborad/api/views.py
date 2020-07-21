import pytz
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from dashborad.models import Health, Patient, HourlyHeartRate, WeeklyHealthSummary, MinuteHeartRate
from dashborad.api.serializer import HeartRateSerializer, PatientSerializer, HealthSerializer, HourlyHeartRateSerializer,HealthSummarySerializer
from dashborad.api.filters import HealthFilter

from django.core import serializers
from django.utils.dateparse import parse_date
from django.db.models import Avg, Max, Min, Sum
from datetime import datetime, date, time, timedelta

from django.http import JsonResponse
from django.db import connections
import json


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/health-list/<int:pk>/',
        'PatientsList': 'health-patients/',
        'Health-PatientHeartRatePerMinutePerDay': 'health-PatientHeartRatePerMinutePerDay/<int:pk>/',
        'Health-PatientHeartRatePerHourPerDay': 'health-PatientHeartRatePerHourPerDay/<int:pk>/',
        'health-Summary':'health-Summary/<int:pk>',
        'Daily Summary of Health ':'daily-health-summary/',
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
        endDate = startDate + timedelta(days=1)

        hourlyrate = HourlyHeartRate.objects.hourly_avg_rate(pk, startDate, endDate)

        serializer = HourlyHeartRateSerializer(hourlyrate, many=True)
        return Response(serializer.data)



# @api_view(['GET'])
# def healthSummary(request,pk):
#     if request.method == 'GET':
#         strDate = request.query_params.get('strDate', None)
#         # date_str = parse_date(strDate)
#         # date_obj = datetime.strptime(date_str, '%Y-%m-%d')
#         date_obj= parse_date(strDate)
#         start_of_week = date_obj - timedelta(days=date_obj.weekday())  # Monday
#         end_of_week = start_of_week + timedelta(days=6)  # Sunday

#         weekly_avg_hearrate = Health.objects.filter(time__lte=end_of_week,time__gt=start_of_week.timedelta(days=7)).values('value').aggregate(Avg('value'))
#         # all_data=Health.objects.all()
#         # weekly_avg_hearrate=Health.objects.filter(time__lte=start_of_week - timedelta(days=7),time__lt=start_of_week).aggregate(average_price=Avg('value'))
#         # weekly_avg_hearrate=Health.objects.filter(time__range=[start_of_week, end_of_week])
#         serializer=HealthSummarySerializer(weekly_avg_hearrate,many=True)
#         return Response(serializer.data)

# @api_view(['GET'])
# def healthSummary(request, pk):
#     if request.method == 'GET':
#         strDate = request.query_params.get('strDate', None)

#         date_obj= parse_date(strDate)


#         start_of_week = date_obj - timedelta(days=date_obj.weekday())  # Monday
#         end_of_week = start_of_week + timedelta(days=6)  # Sunday 6

#         weeklyhealthSummary = WeeklyHealthSummary.objects.weeklyHealthSummary_average(pk, start_of_week, end_of_week)
#         serializer = HealthSummarySerializer(weeklyhealthSummary, many=True)
#         return Response(serializer.data)

@api_view(['GET'])
def healthSummary(request, pk):
    if request.method == 'GET':
        json_data = []
        strDate = request.query_params.get('strDate', None)
        from django.db import connection

        date_obj= parse_date(strDate)

        startdate= date_obj - timedelta(days=date_obj.weekday())  # Monday
        enddate= start_of_week + timedelta(days=6)  # Sunday 6
        
        with connection.cursor() as cursor:
            cursor.execute(""" SELECT avg(value) HeartRate, AVG(Intensity) Intensity,AVG(SleepValue) AS Sleep 
            ,Min(value) as MinHeartReate,Max(value) as MaxHearRate
            FROM `dashborad_health`  where Id=%s and (Time BETWEEN %s AND %s ) """, (pid, startdate, enddate))
            objs = cursor.fetchall()
            for obj in objs:
                json_data.append({"AverageHeartReate" : obj[0], "Average" : obj[1],"Sleep":obj[2],"WalkTime":obj[3],"CaloriesBurnTime":obj[4],"EngeryExpendTime":obj[5],"Activity":obj[6],"WorkoutTime":obj[7],"CaloriesConsumed":obj[8]})
        return JsonResponse(json_data, safe=False)

           


@api_view(['GET'])
def dailyHealthSummary(request):
    json_data = []
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("""SELECT DATE(Time) AS date, avg(value) AS AverageHeartRate, DATE_FORMAT(SleepMinute,'%H:%i') as Sleep,DATE_FORMAT(StepsMinute,'%H:%i')  as WalkTime,DATE_FORMAT(CalMinute,'%H:%i')  as CaloriesBurnTime, DATE_FORMAT(MetMinute,'%H:%i')  as EngeryExpendTime,IF(Mets < 3, 'Light Activity', IF(Mets>6,'Vigorous Activity',IF((Mets<=3 and MEts <=6),'Moderate Activity',''))) as Activity,DATE_FORMAT(IntensityTime,'%H:%i') as WorkoutTime,Calories as CaloriesConsumed FROM dashborad_health GROUP BY date order by date asc;""")
        objs = cursor.fetchall()    
        for obj in objs:
            json_data.append({"date" : obj[0], "AverageHeartRate" : obj[1],"Sleep":obj[2],"WalkTime":obj[3],"CaloriesBurnTime":obj[4],"EngeryExpendTime":obj[5],"Activity":obj[6],"WorkoutTime":obj[7],"CaloriesConsumed":obj[8]})
    return JsonResponse(json_data, safe=False)
