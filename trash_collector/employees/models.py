from django.db import models


class Employee(models.Model):
    user = models.OneToOneField('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=50)
    address = models.CharField(max_length=250)


class Pickup(models.Model):
    customer = models.ForeignKey('customers.Customer', blank=True, null=True, on_delete=models.CASCADE)
    employee = models.ForeignKey('employees.Employee', blank=True, null=True, on_delete=models.CASCADE)
    pickup_date = models.DateField(null=True, blank=True)
