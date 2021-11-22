from django.shortcuts import render, redirect
from collections import OrderedDict
from django.shortcuts import render

from categories.models import Category
from tasks.models import Task
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.http import JsonResponse
from django.core.serializers import serialize
from tasks.form import *


def home(request):
    Task.objects.filter(user=request.user.id)
    return render(request, 'home.html')


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    form_class = AddTaskForm
    success_url = reverse_lazy('board')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)



class TaskListView(ListView, LoginRequiredMixin):
    model = Task
    context_object_name = 'listTasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listTasks'] = context['listTasks'].filter(user=self.request.user)
        return context

    # if json param is passed, return a json
    def get(self, request, *args, **kwargs):
        if 'json' in self.request.GET:
            queryset = self.get_queryset()
            data = serialize("json", queryset)
            return JsonResponse(data, status=200, safe=False)
        else:
            return super().get(self, request, *args, **kwargs)


def jsonTasks(request, id):
    data = serialize("json", Task.objects.filter(user=id))
    return JsonResponse(data, status=200, safe=False)


class UpdateTask(UpdateView, LoginRequiredMixin):
    model = Task
    form_class = UpdateTaskForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('board')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs



def deleteTask(request, id):
    model = Task.objects.filter(id=id)
    model.delete()
    return redirect('board')


def board(request, id=None):
    #get categeroies to show in navbar
    categories = Category.objects.filter(user=request.user.id)

    #tasks to show
    task_list = OrderedDict()

    #filters for tasks
    filterCategory = {}

    #filter by category
    if id is not None:
        filterCategory = {'category': id}

    #idk how to do this less ugly
    for status, status_n in Task.Status.choices:
        task_list[status_n] = Task.objects.filter(user=request.user.id, status=status, **filterCategory)

    print(task_list)

    return render(request, 'board.html', {'categories': categories, 'tasks': task_list, 'category':id})
