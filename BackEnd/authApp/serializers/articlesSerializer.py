from authApp.models.articles import Articles
from rest_framework import serializers


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ['article_id', 'article_img', 'title', 'publication_date']
