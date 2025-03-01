from django.db import models

class Plot(models.Model):
    title = models.CharField(unique=True, max_length=200)
