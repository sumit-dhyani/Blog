from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    Title=models.CharField(max_length=100)
    Description = models.TextField()
    Date=models.TimeField()

    def get_absolute_url(self):
        return reverse("posts",kwargs={'pk':self.id})