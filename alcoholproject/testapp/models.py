from django.db import models
from django.urls import reverse
# Create your models here.
class Alcohol(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    percent=models.FloatField()
    price=models.FloatField()

def get_absolute_url(self):
    return reverse('detail',kwargs={'pk':self.pk})