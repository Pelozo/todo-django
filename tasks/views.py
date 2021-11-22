import serializers as serializers
from django.shortcuts import render
from tasks.models import Task
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.http import JsonResponse
from django.core.serializers import serialize


def home(request):
    Task.objects.filter(user=request.user.id)
    return render(request, 'home.html')


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'category']
    success_url = reverse_lazy('home')

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
    print(data)
    return JsonResponse(data, status=200, safe=False)


class JsonTaskListView(ListView):
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
