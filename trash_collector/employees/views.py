from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.apps import apps
from customers.models import Customer
from .models import Pickup,Employee
from datetime import datetime

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')


def daily_view(request):
    user = request.user
    employee = get_object_or_404(Employee,user=user)
    zipcode = employee.zipcode
    print('zipcodeee',zipcode)
    print('employee',employee)
    if request.method == 'GET':
        if 'id' in request.GET:
            pickup = Pickup.objects.create(employee=user.employee, customer_id=request.GET['id'],
                                           pickup_date=datetime.today())
            customer = Customer.objects.get(id=request.GET['id'])
            customer.balance = customer.balance - 10
            customer.save()
        customers = Customer.objects.filter(zipcode=employee.zipcode)
        print('customersssssssss',customers)
        confirmed_pickup_list = Pickup.objects.filter(is_completed=True)
        print('confirmed_pickup_list',confirmed_pickup_list)
        context={
            'customers': customers,
            'confirmed_pickup_list':confirmed_pickup_list

            }
        return render(request, 'employees/dailyview.html',context )


def PickupIsCompleted(request,id):
    if Customer.objects.filter(id=id).exists():
        customer = get_object_or_404(Customer,id=id)
        Pickup.objects.filter(customer=customer).update(is_completed=True)
        return redirect('employees:dailyview')
    else:
        return redirect('employees:index')