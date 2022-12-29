from django.db import models
from accounts.models import User


class Course(models.Model):
    name = models.CharField(max_length=50)  # it could be primary key as well
    campus = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Request(models.Model):
    student = models.ForeignKey(to=User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=50 , default='')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.course


class Offer(models.Model):
    instructor = models.ForeignKey(to=User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=50 , default = '')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.course
