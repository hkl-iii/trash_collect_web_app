from django.db import models


# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    class WeekDay(models.IntegerChoices):
        MONDAY = 0
        TUESDAY = 1
        WEDNESDAY = 2
        THURSDAY = 3
        FRIDAY = 4
        SATURDAY = 5
        SUNDAY = 6
    name = models.CharField(max_length=50)
    user = models.OneToOneField('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    balance = models.IntegerField(default=0)
    zipcode = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    one_time_pickup = models.DateField(null=True, blank=True)
    weekday = models.IntegerField(default=0, choices=WeekDay.choices)
    pickup_date = models.CharField(max_length=50)
    is_suspended = models.BooleanField(default=False)

    def __str__(self):
        return self.name