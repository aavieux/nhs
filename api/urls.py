from django.urls import path
from . import views

urlpatterns = [
    # path("patients", views.PatientPostListCreate.as_view(), name="patients-view-create"),
    # path("patients/<int:pk>", views.PatientPostRetrieveUpdateDestroy.as_view(), name="update")
    path("", views.index, name="index"),
    path("v1/", views.v1, name="view 1"),
]