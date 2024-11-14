from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    profile_image = models.ImageField(upload_to='./image/profile_image')
    cover_photo = models.ImageField(upload_to='./image/cover_image')
    bio = models.TextField()
    address = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    friends = models.ManyToManyField(User, blank= True, related_name='friend')
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

class RequestModel(models.Model):
    requested_user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='requested_user')
    requested_status = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.requested_user.username}{self.requested_status}"
         