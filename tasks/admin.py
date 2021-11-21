from django.contrib import admin
from categories.models import *
from tasks.models import *

admin.site.register(Category)
admin.site.register(Task)