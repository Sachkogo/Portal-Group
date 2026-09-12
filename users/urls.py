from django.urls import path
from users import views

urlpatterns = [
    path('', views.register_view, name='login'),
]