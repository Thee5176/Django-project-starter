from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from .forms import CustomUserChangeForm
# TODO: Google Sign-in Popup
    
class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ["username","first_name","last_name","gender","occupation","city","annual_income"]
    success_url = reverse_lazy("home")
    template_name = "profile.html"