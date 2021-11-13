from django.contrib.auth.models import User
from django.db import models

class SystemUser(User):
    age = models.IntegerField()
    friends = models.ManyToManyField("self")
