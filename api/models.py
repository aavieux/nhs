from django.db import models


# Create your models here.
# models.Model is a predefined django class for DB objects
class Hospital(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.TextField()
    contact_info = models.TextField()

    class Meta:
        db_table = 'hospital'
    def __str__(self):
        return self.name


class Patient(models.Model):
    class Gender(models.TextChoices):
        MALE = "Male",
        FEMALE = "Female",
        OTHER = "Other"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_info = models.TextField()
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=6,
        choices=Gender.choices
    )
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'patient'
    def __str__(self):
        return self.name


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

    class Meta:
        db_table = 'department'
    def __str__(self):
        return self.name
class HealthCareProf(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'healthcare_professional'

    def __str__(self):
        return f"{self.name} ({self.department})"

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    healthCareProf = models.ForeignKey(HealthCareProf, on_delete=models.SET_NULL, null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    date = models.DateTimeField(null=True)

    class Meta:
        db_table = 'appointment'

    def __str__(self):
        patient_name = self.patient.name if self.patient else "Unknown"
        hcp_name = self.healthCareProf.name if self.healthCareProf else "Unknown"
        hospital_name = self.hospital.name if self.hospital else "Unknown"
        department_name = self.department.name if self.department else "Unknown"
        return f"Appointment ID: {self.id} Patient name: {patient_name} - Doctor name: {hcp_name} - Hospital name: {hospital_name} - Department name: {department_name} - Date: {self.date}"


class MedicalRecord(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'medical_record'
    def __str__(self):
        return self.patient.name
class MedicalCase(models.Model):
    id = models.AutoField(primary_key=True)
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.SET_NULL, null=True)
    healthCareProf = models.ForeignKey(HealthCareProf, on_delete=models.SET_NULL, null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=10000)
    treatment = models.TextField(max_length=10000)

    class Meta:
        db_table = 'medical_case'

    def __str__(self):
        return f"(Medical case number: {self.id} {self.medical_record.patient.name} {self.healthCareProf.name} {self.hospital.name} {self.department} {self.date})"