from django.db import models
from user.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    category = models.IntegerField()
    status = models.CharField(max_length=15)
    #tags = models.ManyToManyField()