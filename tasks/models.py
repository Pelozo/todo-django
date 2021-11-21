from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


class Task(models.Model):
    class Status(models.TextChoices):
        TO_DO = 'to do'
        IN_PROGRESS = 'in progress'
        FINISHED = 'finished'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    status = models.CharField(max_length=15, default=Status.TO_DO, choices=Status.choices)

    # tags = models.ManyToManyField()
