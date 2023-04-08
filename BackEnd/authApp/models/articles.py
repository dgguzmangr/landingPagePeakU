from django.db import models


class Articles(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_img = models.ImageField(upload_to='articles')
    title = models.CharField('Title', max_length=200)
    publication_date = models.DateField('Date', null=True)
