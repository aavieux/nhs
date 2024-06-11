from django.contrib import admin
from api.models import *
# Register your models here.
admin.site.register(Patient)
admin.site.register(Hospital)
admin.site.register(Appointment)
admin.site.register(HealthCareProf)
admin.site.register(Department)
admin.site.register(MedicalCase)
admin.site.register(MedicalRecord)
