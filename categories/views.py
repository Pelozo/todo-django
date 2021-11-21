from categories.models import Category
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['title']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CategoryCreate, self).form_valid(form)

"""def create_category(request):
    if request.method == 'GET':
        form = CategoryForm()
        contexto = {
            'form': form
        }
    else:
        form =CategoryForm(request.POST)
        contexto = {
            'form': form
        }
        
        if form.is_valid():
            form.save()
            return redirect('home.html')
    return render(request, 'categories/create_category.html', contexto)"""