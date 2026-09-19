from django.shortcuts import render
from .models import  Grade
# Create your views here.
def diary_list(request):
    grades = Grade.objects.all()
    
    return render(request, "grades/diary_list.html", {"grades": grades})