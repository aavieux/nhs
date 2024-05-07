from rest_framework import serializers
from .models import Hospital, Patient

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ["id", "name", "location", "contact_info"]
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id", "name", "address", "contact_info", "date_of_birth", "gender", "registration_date"]