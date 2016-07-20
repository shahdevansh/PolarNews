from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView, TemplateView

from models import NewsArticle, Tag

article_list = ListView.as_view(model=NewsArticle)

urlpatterns = patterns('',
        url(r'^feed', article_list, name='List of Articles'),
        url(r'', TemplateView.as_view(template_name="index.html"), name='Home Page')
)
