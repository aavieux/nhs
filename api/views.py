from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authentication import authenticate
from rest_framework.authtoken.views import obtain_auth_token
from .models import Hospital, Patient
from .serializers import HospitalSerializer, PatientSerializer
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
def index(response):
    return HttpResponse("tech with tim!")
def v1(response):
    return HttpResponse("view 1")