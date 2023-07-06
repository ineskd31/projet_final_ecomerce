from django.db import models

# Create your models here.
class Contact(models.Model):
    location = models.CharField(max_length=500)
    number = models.CharField(max_length=50)
    email = models.EmailField()
    