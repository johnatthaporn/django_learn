from django.shortcuts import render
from django.views.generic import FormView, CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from accounts.forms import UserCreateForm
# Create your views here.
class SignupView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')
