from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authentication import authenticate
from rest_framework.authtoken.views import obtain_auth_token
from .models import *
# from .serializers import HospitalSerializer, PatientSerializer
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse

# Create your views  here.
# OBJECT RELATIONAL MAPPING
# class HospitalPostListCreate(generics.ListCreateAPIView):
#     queryset = Hospital.objects.all()  # gets all hospital objects from the api
#     serializer_class = HospitalSerializer
#
#
# class PatientPostListCreate(generics.ListCreateAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer
#
#     def delete(self, request, *args, **kwargs):
#         Patient.objects.all().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# # generic views are crated by django as a default view template
# class PatientPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer
#     lookup_field = "pk"
def index(response): # /
    hospital = Hospital.objects.get(id = 1)
    return render(response, "nhs/home.html", {"name": hospital.name})
def base(response):
    return render(response, "nhs/base.html", {})
def viewPatient(response, id): # /patient/x
    patient = Patient.objects.get(id=id)
    appointment = patient.appointment_set.all()[0]
    # return HttpResponse("<h1>%s<h1/>" % str(appointment))
    return render(response, "nhs/patient.html", {"patient": patient, "appointment": appointment})


# def home(response):

