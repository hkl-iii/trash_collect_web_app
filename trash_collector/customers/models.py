from django.db import models
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    pickup_date = models.CharField(max_length=50)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    balance = models.IntegerField(default=0)
    zipcode = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
