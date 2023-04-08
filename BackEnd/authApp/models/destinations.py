from django.db import models
from django.db.models import Avg
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Destinations(models.Model):
    destination_id = models.AutoField(primary_key=True)
    destination_img = models.ImageField(upload_to='destinations')
    country = models.CharField('Country', max_length=30)
    city = models.CharField('City', max_length=30)
    cost = models.PositiveIntegerField('Cost')
    discount_price = models.DecimalField('Discounted price', default=0, max_digits=6, decimal_places=1)
    average_mark = models.DecimalField('Average mark', default=0, max_digits=2, decimal_places=1)

    # discount_price = cost.destinations - cost.destinations*0.15
    def calculate_discount_price(self):
        discount = (self.cost * 0.15)  # 15% discount
        self.discount_price = int(round(self.cost - discount))
        return self.discount_price

    # average_mark = promedio de rating
    def calculate_average_mark(self):
        from .opinions import Opinions
        return Opinions.objects.filter(destination_id=self).aggregate(Avg('rating'))['rating__avg']


@receiver(pre_save, sender=Destinations)
def calculate_discount_price(sender, instance, **kwargs):
    instance.discount_price = instance.calculate_discount_price()


def calculate_average_mark(sender, instance, **kwargs):
    instance.average_mark = instance.calculate_average_mark()















