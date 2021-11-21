from django.shortcuts import render
from tasks.models import Task
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


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
