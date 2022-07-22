from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit-account/', UserEditAccountView.as_view(), name='edit_account'),
    path('password/', UserEditPasswordView.as_view()),
    path('profile/<str:username>', UserProfileView.as_view(), name='profile'),
    path('edit-profile/<str:username>', UserEditProfileView.as_view(), name='edit_profile')
]