from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user}, {self.group}"


class Subject(models.Model):
    subject = models.CharField(max_length=46)

    def __str__(self):
        return self.subject


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')
    grade = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.student} -- {self.subject}: {self.grade}"

