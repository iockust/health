from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from dashborad.models import Health
from dashborad.api.serializer import HealthSerializer



@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/health-list',
        'Detail View':'/health-detail/<str:pk>/',
        'Create':'/health-create',
        'Update':'/health-update/<str:pk>/',
        'Delete':'/health-delete/<str:pk>/',

        # Date Filter
        'Date':'/health-date/',
        ''
        }

    return Response(api_urls)



@api_view(['GET'])
def healthDateFilter(request):
    try:
        # health=Health.objects.get(slug=slug)
        #health=Health.objects.all()
        # health = Health.objects.raw('select `Id` as id, `Time`,`Value`,`IntensityTime`,`Intensity`,`StepsMinute`,`Steps`,`SleepMinute`,`SleepValue`,`SleepLogId`,`MetMinute`,`METs`,`CalMinute`,`Calories` from `dashborad_health` where id=2026352035 limit 4')
        health=Health.objects.filter(id=pk)[:3]   
    
    except Health.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer=HealthSerializer(health,many=True)
        return Response(serializer.data)



@api_view(['GET'])
def healthList(request):
    try:
        # health=Health.objects.get(slug=slug)
        #health=Health.objects.all()
        # health = Health.objects.raw('select `Id` as id, `Time`,`Value`,`IntensityTime`,`Intensity`,`StepsMinute`,`Steps`,`SleepMinute`,`SleepValue`,`SleepLogId`,`MetMinute`,`METs`,`CalMinute`,`Calories` from `dashborad_health` where id=2026352035 limit 4')
        health=Health.objects.filter(id=pk)[:3]   
    
    except Health.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer=HealthSerializer(health,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def healthDetial(request,pk):
    try:
        # health=Health.objects.get(slug=slug)
         health=Health.objects.get(id=pk)   
    
    except Health.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method=="GET":
        serializer=HealthSerializer(health,many=False)
        return Response(serializer.data)
 



# Update
@api_view(['POST'])
def healthUpdate(request,pk):

    try:
        health =Health.objects.get(id=pk)
    
    except Health.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="POST":
        serializer=HealthSerializer(instance=health,data=request.data)
        data={}

        if serializer.is_valid():
            serializer.save()
            data["success"]="update sucessful"
            return Response(data=data)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def healthDelete(request,pk):

    try:
        health =Health.objects.get(id=pk)
    
    except Health.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="DELETE":
        operation=health.delete()
        data={}

        if operation:
            data['successs']="delete successful"
        
        else:
            data["failure"]="delete failed "

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

 

# Create
@api_view(['POST'])
def healthCreate(request):

    if request.method=='POST':
        serializer=HealthSerializer(data=request.data)
        data={}

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        



