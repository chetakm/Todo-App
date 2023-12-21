from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.title
