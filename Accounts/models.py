from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='User/Img/%y/%m/%d', default='user.jpg', blank=True)
    about = models.TextField(blank=True)
    phone = models.IntegerField(blank=True)

    city = models.CharField(max_length=40, blank=True)
    state = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=40, blank=True)




