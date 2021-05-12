from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from customers.models import Customer
from .models import Pickup
from datetime import datetime


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')


def daily_view(request):
    user = request.user
    if request.method == 'GET':
        if 'id' in request.GET:
            pickup = Pickup.objects.create(employee=user.employee, customer_id=request.GET['id'],
                                           pickup_date=datetime.today())
            customer = Customer.objects.get(id=request.GET['id'])
            customer.balance = customer.balance - 10
            customer.save()
        customers = Customer.objects.filter(zipcode=user.employee.zipcode, start_date__isnull=True,
                                            pickup_date=datetime.today())
        return render(request, 'employees/dailyview.html', context={'customers': customers})
