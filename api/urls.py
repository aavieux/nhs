from django.urls import path
from . import views

urlpatterns = [
    path("patients", views.PatientPostListCreate.as_view(), name="patients-view-create"),
    path("patients/<int:pk>", views.PatientPostRetrieveUpdateDestroy.as_view(), name="update")
]