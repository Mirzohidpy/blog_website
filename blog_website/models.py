from asyncio.base_subprocess import WriteSubprocessPipeProto
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150, default='This is the blog of mine that posts usefull info about programming language pythone')
    profile_image = models.ImageField(upload_to='photo/profile/%Y/%m/%d', blank=True)
    phone = models.CharField(max_length=50, default='----------------', blank=True)
    mobile = models.CharField(max_length=50, default='----------------', blank=True)
    adress = models.CharField(max_length=100, default='Uzbekistan', blank=True)
    website_url = models.CharField(max_length=255, default='#', blank=True)
    github_url = models.CharField(max_length=255, default='#', blank=True)
    instagram_url = models.CharField(max_length=255, default='#', blank=True)
    facebook_url = models.CharField(max_length=255, default='#', blank=True)
    telegram_url = models.CharField(max_length=255, default='#', blank=True)


    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    def image_url(self):
        try:
            url = self.profile_image.url  
        except:
            url = 'https://pic.onlinewebfonts.com/svg/img_569204.png'
        return url