from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from account.forms import RegistrationForm
from account.models import User


class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'account/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('homepage')
    success_message = 'Аккаунт успешно создан!!!'


class SignInView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('homepage')


def profile(request):
    return render(request, 'account/profile.html')







