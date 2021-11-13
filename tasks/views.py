from django.shortcuts import render
from tasks.models import Task


def home(request):
    Task.objects.filter(user = request.user.id)
    return render(request, 'home.html')