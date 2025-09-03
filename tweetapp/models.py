from django.db import models

# Create your models here.
class Tweet(models.Model):
    nick_name = models.CharField(max_length=50)
    massage = models.CharField(max_length=280)

    def __str__(self):
        return f"Tweet nick: {self.nick_name} massage: {self.massage}"