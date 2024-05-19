
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):

    class Language(models.IntegerChoices):
        ES = 0
        EN = 1

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    avatar = models.ImageField(upload_to='user/avatar')
    language = models.IntegerField(choices=Language, default=Language.ES)
    age = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=200, default='')