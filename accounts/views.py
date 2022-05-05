from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("auth-login")
    template_name = "accounts/signup.html"


def profile(request):
    return render(request, "accounts/profile.html")
