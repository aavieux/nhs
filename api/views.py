from django.shortcuts import render
from rest_framework import generics
from .models import Hospital, Patient
from .serializers import HospitalSerializer, PatientSerializer
# Create your views here.

#OBJECT RELATIONAL MAPPING
class HospitalPostListCreate(generics.ListCreateAPIView):
    queryset = Hospital.objects.all() #gets all hospital objects from the api
    serializer_class = HospitalSerializer

class PatientPostListCreate(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
#generic views are crated by django as a default view template
class PatientPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = "pk"