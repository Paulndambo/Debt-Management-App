from django.db import models
from .constants import UNIT_CHOICES
from django.urls import reverse

# Create your models here.
class AbstractBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Inventory(AbstractBaseModel):
    name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=2)
    unit = models.CharField(max_length=255, choices=UNIT_CHOICES)
    installment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("items")