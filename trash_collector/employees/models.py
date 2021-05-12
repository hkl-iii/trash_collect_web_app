from django.db import models


class Employee(models.Model):
    user = models.OneToOneField('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
