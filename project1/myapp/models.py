from django.db import models

# Create your models here.
class Detail(models.Model):
    Choice=models.CharField(max_length=7)