from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .destinations import Destinations


class Promotions(models.Model):
    promotion_id = models.AutoField(primary_key=True)
    destination_id = models.ForeignKey(Destinations, on_delete=models.CASCADE)
    trip_length = models.PositiveIntegerField('Length', validators=[MinValueValidator(5), MaxValueValidator(15)])
    plan_cost = models.PositiveIntegerField('Promotional cost', default=0)

    # plan_cost = discount_price.destinations * trip_length.promotions
    def calculate_plan_cost(self):
        discount_price = self.destination_id.discount_price
        trip_length = self.trip_length
        self.plan_cost = discount_price * trip_length
        return self.plan_cost


@receiver(pre_save, sender=Promotions)
def calculate_plan_cost(sender, instance, **kwargs):
    instance.plan_cost = instance.calculate_plan_cost()
