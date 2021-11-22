from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.template.loader import render_to_string
from user.forms import UserForm
from django.contrib.auth import logout

def loginView(request):
    if request.method == 'POST':
        # sends the data to the DB in order to retrieve data matched with request data
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # retrieves the user from the valid form
            login(request, user)  # uses imported django built in login to log the user
            return redirect('/home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logoutView(request):
    logout(request)
    return redirect('/home')

class Register(CreateView):
    model = User
    form_class = UserForm
    template_name = 'registration/register.html'
    success_url = '/'

    def get_success_url(self):
        # send welcome email
        msg_plain = render_to_string('emails/welcome.txt', {'name': self.object.first_name})
        msg_html = render_to_string('emails/welcome.html', {'name': self.object.first_name})
        send_mail(
            subject='Welcome!',
            message=msg_plain,
            from_email=None,
            recipient_list=[self.object.email],
            html_message=msg_html,
            fail_silently=False,
        )
        # login the person
        self.object.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, self.object)
        # now return the success url
        return '/'
