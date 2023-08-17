from django.db import models
from core.models import AbstractBaseModel
from django.urls import reverse
# Create your models here.
GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)

class Customer(AbstractBaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True)
    id_number = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    def get_absolute_url(self):
        return reverse("customers")


    def name(self):
        return f"{self.first_name} {self.last_name}"