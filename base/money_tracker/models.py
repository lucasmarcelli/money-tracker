from django.db import models

from django.conf import settings


# Create your models here.
class Line(models.Model):
    date = models.DateField()
    user = user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
        )
    item = models.TextField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    reason = models.TextField()
    unneccesary = models.BooleanField()
    company = models.TextField()
