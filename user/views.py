from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView


# silvania 1234
class Login(LoginView):
    template = 'login.html'


class Register(CreateView):
    template = 'register.html'
    success_message = "Your profile was created successfully"
