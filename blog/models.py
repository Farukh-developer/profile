from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image=models.ImageField(upload_to='profile_pics/', null=True, blank=True, default="profile_pics/default.jpeg")
    phone_number=models.CharField(max_length=100)
    address=models.CharField(max_length=100)


class Student(models.Model):
    name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(max_length=120)
    

    def __str__(self):
        return f"{self.name}"
