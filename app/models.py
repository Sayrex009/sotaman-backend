# app/models.py
from django.db import models

class user(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    is_authenticated = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class category(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Subscription(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    plan = models.CharField(max_length=100)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.plan}"