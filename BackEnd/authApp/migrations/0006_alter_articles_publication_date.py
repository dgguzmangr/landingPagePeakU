# Generated by Django 4.1.7 on 2023-04-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0005_alter_articles_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='publication_date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
    ]
