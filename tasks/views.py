from django.shortcuts import render, redirect
from tasks.models import Task
from .form import TaskForm


def home(request):
    Task.objects.filter(user=request.user.id)
    return render(request, 'home.html')

def create_task(request):
    if request.method == 'GET':
        form = TaskForm()
        contexto = {
            'form': form
        }
    else:
        form =TaskForm(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('home.html')
    return render(request, 'tasks/create_task.html', contexto)