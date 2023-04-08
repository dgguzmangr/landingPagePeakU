from django.db import models


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_img = models.ImageField(upload_to='customers')
    name = models.CharField('Name', max_length=200, null=True)
    last_name = models.CharField('Last name', max_length=200, null=True)
    email = models.EmailField('E-mail', max_length=200, null=True)
