from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class SignupView(FormView):
  form_class = UserCreationForm
  template_name = 'signup.html'
  success_url = '/login'

  def form_valid(self, form):
    form.save()
    return super().form_valid(form)