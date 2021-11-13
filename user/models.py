from django.contrib.auth.models import User
from django.db import models

class SystemUser(User):
    friends = models.ManyToManyField("self")
