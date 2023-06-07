from django.db import models

# Create your models here.
class AutoPlot_model(models.Model):
  runtime = models.DateField()
  action = models.CharField(max_length=255)