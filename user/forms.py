from django import forms


class LoginForm(forms.form):
    email = forms.CharField()
    password = forms.PasswordInput()
