from django.db import models

from django.conf import settings


# Create your models here.
class Line(models.Model):
    date = models.DateField()
    user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
        )
    item = models.TextField()
    amount_out = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    amount_in = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    reason = models.TextField()
    unnecessary = models.BooleanField()
    company = models.TextField()
