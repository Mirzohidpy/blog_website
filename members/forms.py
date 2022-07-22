from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from blog_website.models import *
from blog_website.models import Profile
 

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label = 'Repeat Password')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



class EditAccountForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')



class EditPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Old Password')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password')

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class EditProfileForm(forms.ModelForm):
    class Meta:
         model = Profile
         fields = ('bio', 'phone', 'profile_image', 'mobile', 'adress', 'website_url', 'github_url', 'telegram_url', 'instagram_url', 'facebook_url')
         widgets = {
            'bio' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'mobile' : forms.TextInput(attrs={'class':'form-control'}),
            'adress' : forms.TextInput(attrs={'class':'form-control'}),
            'website_url' : forms.TextInput(attrs={'class':'form-control'}),
            'github_url' : forms.TextInput(attrs={'class':'form-control'}),
            'telegram_url' : forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url' : forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url' : forms.TextInput(attrs={'class':'form-control'}),
         }
         
