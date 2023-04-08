# Generated by Django 4.1.7 on 2023-04-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinations',
            name='average_mark',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Average mark'),
        ),
        migrations.AlterField(
            model_name='destinations',
            name='discount_price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=6, verbose_name='Discounted price'),
        ),
    ]
