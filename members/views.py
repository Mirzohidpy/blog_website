from unicodedata import name
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView, TemplateView, ListView
from django.contrib.auth.views import  PasswordChangeView
from django.urls import reverse_lazy
from requests import request
from blog_website.models import Profile
from members.forms import RegisterForm, EditAccountForm, EditPasswordForm, EditProfileForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User 
# Create your views here.

class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'registration/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    success_message = "Registration was succefully completed!!"

class UserEditAccountView(SuccessMessageMixin, UpdateView):
    form_class = EditAccountForm
    template_name = 'registration/edit_account.html'
    success_url = reverse_lazy('edit_account')
    success_message = "Account data was succefully updated!!"

    def get_object(self):
        return  self.request.user


class UserEditPasswordView(SuccessMessageMixin, PasswordChangeView):
    form_class = EditPasswordForm
    template_name = 'registration/edit_password.html'
    success_url = reverse_lazy('edit_account')
    success_message = "Password was succefully changed!!"


class UserProfileView(ListView):
    model = Profile
    template_name = 'registration/profile.html'


    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=(self.kwargs['username']))
        user_profile, created = self.model.objects.get_or_create(user=user)
        context = super().get_context_data(**kwargs)
        context['user_profile'] = user_profile
        return context 



class UserEditProfileView(SuccessMessageMixin, UpdateView):
    form_class = EditProfileForm
    model = Profile
    template_name = 'registration/edit_profile.html'
    success_message = "Profile data was successfully updated!!"

    def get_success_url(self) -> str:
        return reverse_lazy('profile', kwargs={'username':self.request.user.username})

    
    def get_object(self):
        return get_object_or_404(self.model, user=self.request.user)