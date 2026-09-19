from django.urls import path
from .views import event_list
from .views import calendar_view

urlpatterns = [
    path('', event_list, name='event_list'),
    path('calendar/', calendar_view, name='calendar'),
]