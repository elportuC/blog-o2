from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name="registration/signup.html"
    success_url = reverse_lazy("login")
    
    class LogoutView(TemplateView):
        template_name = "logout.html"

