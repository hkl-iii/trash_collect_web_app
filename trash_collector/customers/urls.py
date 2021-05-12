from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('setpickup/', views.pickup, name='setpickup'),
    path('suspendpickup/', views.suspend, name="suspendpickup"),
    path('accountinfo/', views.detail, name='accountinfo'),
    path('requestapickup/', views.one_time_pickup, name='requestapickup'),
    path('registercustomer/', views.create, name='registercustomer')
]
