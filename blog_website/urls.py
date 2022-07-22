from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('listing-page/', listing_page, name='listing'),
    path('post-page/', post_page, name='post'),
    path('test-page/', test_page, name='test'),
]