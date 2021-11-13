from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from user.models import SystemUser
from django.urls import reverse


# silvania 1234
class Login(LoginView):
    model = SystemUser
    template = 'login.html'


class Register(CreateView):
    model = SystemUser
    #fields = '__all__'
    fields = ['username', 'email', 'first_name', 'last_name', 'password']
    template_name = 'registration/register.html'

    def get_success_url(self):
        return reverse('home')
