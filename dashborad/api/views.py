from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from dashborad.models import Health, Patient
from dashborad.api.serializer import HealthFilterSerializer, PatientSerializer, HealthSerializer
from dashborad.api.filters import HealthFilter
from django.utils.dateparse import parse_date
import datetime

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/health-list/<int:pk>/',
        'Detail View': '/health-detail/<str:pk>/',
        'Create': '/health-create',
        'Update': '/health-update/<str:pk>/',
        'Delete': '/health-delete/<str:pk>/',
        'PatientsList': 'health-patients/',
        'Health-heartrate':'health-heartrate/'
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


@api_view(['GET'])
def healthDetial(request, pk):
    try:
        # health=Health.objects.get(slug=slug)
        health = Health.objects.get(id=pk)[:1]

    except Health.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = HealthSerializer(health, many=False)
        return Response(serializer.data)


# Update
@api_view(['POST'])
def healthUpdate(request, pk):
    try:
        health = Health.objects.get(id=pk)

    except Health.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        serializer = HealthSerializer(instance=health, data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()
            data["success"] = "update sucessful"
            return Response(data=data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def healthDelete(request, pk):
#     try:
#         health = Health.objects.get(id=pk)
#
#     except Health.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "DELETE":
#         operation = Healthdata.delete()
#         data = {}
#
#         if operation:
#             data['successs'] = "delete successful"
#
#         else:
#             data["failure"] = "delete failed "
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create
@api_view(['POST'])
def healthCreate(request):
    if request.method == 'POST':
        serializer = HealthSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
def  healthHeartRate(request):
    if request.method=='GET':
        startdate=request.data.get('startdate')
        enddate=request.data.get('enddate')
        # filter_data = HealthFilter(request.GET, queryset=Health.objects.all())
        filter_data=Health.objects.filter(date__range=[startdate, enddate])
        serializer=HealthFilterSerializer(filter_data,many=True)
        return Response(serializer.data)
    # except Patient.date_error_message