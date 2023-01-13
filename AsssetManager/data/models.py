from datetime import datetime
from django.db import models

# Create your models here.

spec_choices=(
    ("Good","Good"),
    ("Bad","Bad")
)
class Asset(models.Model):
    name=models.CharField(max_length=100)
    specifications=models.CharField(max_length=100)
    condition=models.CharField(max_length=100,choices=spec_choices)
    location=models.CharField(max_length=100)
    date_entered=models.DateField(null=True)

    def __str__(self):

        return self.asset


class EmployeeAsset(models.Model):
    name=models.CharField(max_length=100)
    specifications=models.CharField(max_length=100)
    condition=models.CharField(max_length=100,choices=spec_choices)
    location=models.CharField(max_length=100)
    date_entered=models.DateField(null=True)

    def __str__(self):

        return self.asset