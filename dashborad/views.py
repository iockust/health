from django.views.generic import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse
from .models import Health
from django.core import serializers

from pandas_profiling import ProfileReport
import pandas as pd
import numpy as np
class MainPageView(View):
    def get(self,request,*args,**kwargs):

        """Main URL to test Chart.js"""

        n, bins = 10000, 20
        normal = np.random.normal(0, 1, n)
        gumbel = np.random.gumbel(0, 1, n)
        weibull = np.random.weibull(5, n)
        nhistogram = np.histogram(normal, bins=bins)
        ghistogram = np.histogram(gumbel, bins=bins)
        whistogram = np.histogram(weibull, bins=bins)
        
        return render(request,'dashborad/main.html',nvalues=nhistogram[0].tolist(),
							nlabels=nhistogram[1].tolist(),
							ncolor='rgba(50, 115, 220, 0.4)',
							gvalues=ghistogram[0].tolist(),
							glabels=ghistogram[1].tolist(),
							gcolor='rgba(0, 205, 175, 0.4)',
							wvalues=whistogram[0].tolist(),
							wlabels=whistogram[1].tolist(),
							wcolor='rgba(255, 56, 96, 0.4)')


class ChartsPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashborad/charts2.html')

class ChartsData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "labels": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "data": [12, 19, 3, 5, 2, 3, 10],
        }   

        return Response(data)



class ReportPageView(View):
    def get(self,request,*args,**kwargs):
        # dataset=pd.DataFrame.from_records(Health.objects.all().values())
        # # dataset = Health.objects.all()
        # prof = ProfileReport(dataset)
        # prof.to_file(output_file='dashborad/report.html')
        return render(request,'dashborad/report.html')
