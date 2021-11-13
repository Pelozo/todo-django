from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView

"""
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # TODO redirect to home
            return
        else:
            return render(request, 'login.html')
            # TODO redirect to login with flag
            
"""


class login(LoginView):
    template = 'login.html'
