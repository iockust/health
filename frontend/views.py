from django.shortcuts import render
from backend.models import Patient
from django.views.generic import View
# Create your views here.

class MainPageView(View):
    def get(self, request, *args, **kwargs):
        patients = Patient.objects.all()
        return render(request, 'main.html', {'patients': patients})

class ContactPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html')

class ActivitesPageView(View):
    def get(self, request, *args, **kwargs):
        patients = Patient.objects.all()
        return render(request, 'activities.html', {'patients': patients})
