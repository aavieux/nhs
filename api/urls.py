from django.urls import path
from django.views.generic import RedirectView

from . import views
from .models import *
urlpatterns = [
    # path("patients", views.PatientPostListCreate.as_view(), name="patients-view-create"),
    # path("patients/<int:pk>", views.PatientPostRetrieveUpdateDestroy.as_view(), name="update")
    # path('', RedirectView.as_view(url='/admin/', permanent=True)),
    # path("home/", views.home, name="home")
]