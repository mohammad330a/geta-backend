from django.db import models
from django.contrib.auth.models import User


class Courses(models.Model):
    name = models.CharField(max_length=50)  # it could be primary key as well(it helps the proces of )
    campus = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Requests(models.Model):
    student = models.ForeignKey(to=User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.course


class Offers(models.Model):
    instructor = models.ForeignKey(to=User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.course
