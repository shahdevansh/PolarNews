from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField

# Create your models here.
class Tag(models.Model):
    term = models.CharField(max_length=250)
    scheme = models.URLField(max_length=500)
    labels = models.CharField(max_length=250)

class NewsArticle(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    published = models.CharField(max_length=250)
    aggregated = models.DateTimeField(auto_now_add=True, null=True)
    summary = models.TextField()
    link_to_article = models.URLField(max_length=500)
    tags = ListField(EmbeddedModelField('Tag'))

class MediaSource(models.Model):
    media_id = models.BigIntegerField()
    link_to_source = models.URLField(max_length=500)
    name = models.CharField(max_length=250)
