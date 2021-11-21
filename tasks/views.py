from django.shortcuts import render
from tasks.models import Task
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView


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


"""def create_task(request):
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
    return render(request, 'tasks/create_task.html', contexto)"""
