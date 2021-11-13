from django.contrib.auth.views import LoginView


# silvania 1234
class login(LoginView):
    template = 'login.html'
