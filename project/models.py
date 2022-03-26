from django.db import models
from django.urls import reverse
from datetime import datetime


# Create your models here.
class Blog(models.Model):
    Title=models.CharField(max_length=100)
    Description = models.TextField()
    Date=models.TimeField(default=datetime.now())

    def get_absolute_url(self):
        return reverse("posts",kwargs={'pk':self.id})
    def __str__(self):
        return self.Title