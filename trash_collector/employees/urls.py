from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"

urlpatterns = [
    path('', views.index, name="index"),
    path('dailyview/', views.daily_view, name='dailyview'),
    path('confirm_pickup/<int:id>/', views.PickupIsCompleted, name='confirm_pickup'),

    
]