from django.db import models


# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField
    contact_info = models.TextField

    def __str__(self):
        return self.name


class Patient(models.Model):
    class Gender(models.TextChoices):
        MALE = "Male",
        FEMALE = "Female",
        OTHER = "Other"

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
