from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .customers import Customers
from .destinations import Destinations


class Opinions(models.Model):
    opinion_id = models.AutoField(primary_key=True)
    comment = models.CharField('Comment', max_length=1000)
    rating = models.DecimalField('Rating',
                                 max_digits=2,
                                 decimal_places=1,
                                 validators=[MinValueValidator(0), MaxValueValidator(5)])
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    destination_id = models.ForeignKey(Destinations, on_delete=models.CASCADE)
