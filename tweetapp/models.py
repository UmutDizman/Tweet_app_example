from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    username = models.ForeignKey(User, on_delete= models.CASCADE, null=True)
    massage = models.CharField(max_length=280)

    def __str__(self):
        return f"Tweet nick: {self.username} massage: {self.massage}"