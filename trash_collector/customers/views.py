from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer


# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.
from .. import customers


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    print(user)
    return render(request, 'customers/index.html')


def pickup(request, user_id=None):
    user = request.user
    customer = customers.objects.get(pk=user_id)
    context = {
        'customer':
    }
    if request.method == 'POST':
        print(user)
    return render(request, 'customers/requestpickup.html')
