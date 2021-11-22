from django.shortcuts import redirect

from categories.models import Category
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['title']
    success_url = reverse_lazy('listcategory')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CategoryCreate, self).form_valid(form)


class CategoryListView(ListView, LoginRequiredMixin):
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = context['categories'].filter(user=self.request.user)
        return context

def deleteCategory(request, id):
    model = Category.objects.filter(id=id)
    model.delete()
    return redirect('listcategory')

class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['title']
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listcategory')