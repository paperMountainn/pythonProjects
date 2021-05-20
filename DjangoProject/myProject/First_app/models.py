from django.db import models


# Create your models here.
class First_app(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100)
    summary = models.TextField()
    is_helpless = models.BooleanField(default=True)