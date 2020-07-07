from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from dashborad.models import Health, Patient
from dashborad.api.serializer import HealthFilterSerializer, PatientSerializer
from dashborad.api.filters import HealthFilter
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

        health = Health.objects.filter(id=pk).filter(time__year=2016)[:3]

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

@api_view(['GET'])
def healthHeartRate(request):
    if request.method == 'GET':
        date_input = request.query_params.get('strDate', None)
        pk = request.query_params.get('id')
        health_qs = Health.objects.filter(pk=pk, time__date=date_input)
        serializer = HealthFilterSerializer(health_qs, many=True)
        return Response(serializer.data)