from django.db import models


# Create your models here.
# models.Model is a predefined django class for DB objects
class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.TextField()
    contact_info = models.TextField()

    def __str__(self):
        return self.name


class Patient(models.Model):
    class Gender(models.TextChoices):
        MALE = "Male",
        FEMALE = "Female",
        OTHER = "Other"

    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_info = models.TextField()
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=6,
        choices=Gender.choices
    )
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

class HealthCareProf(models.Model):
    healthCareProf_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL)
class Appointment(models.Model):
    appointment = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL)
    healthCareProf = models.ForeignKey(HealthCareProf, on_delete=models.SET_NULL)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL)
    date = models.DateTimeField()


class MedicalRecord(models.Model):
    medical_record_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL)


class MedicalCase(models.Model):
    medical_case_id = models.AutoField(primary_key=True)
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.SET_NULL)
    healthCareProf = models.ForeignKey(HealthCareProf, on_delete=models.SET_NULL)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=10000)
    treatment = models.TextField(max_length=10000)
