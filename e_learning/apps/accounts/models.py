from django.db import models
from django.contrib.auth.models import AbstractUser


class UserTypes(models.TextChoices):
    STUDENT = "ST", "STUDENT"
    TEACHER = "TC", "TEACHER"


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    user_type = models.CharField(max_length=2, choices=UserTypes.choices, default=UserTypes.STUDENT)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.username
    
    @property
    def display_name(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_subsctiption_active = models.BooleanField(default=False)
    subscription_start_date = models.DateField(null=True, blank=True)
    subscription_end_date = models.DateField(null=True, blank=True)
    num_of_unread_activity_notifications = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_verified = models.BooleanField(default=False)
    num_of_unread_activity_notifications = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username