from django.core.management.base import NoArgsCommand
from newsaggregator.models import Tag, NewsArticle
import json, feedparser, mediacloud

class Command(NoArgsCommand):
    def _get_articles(self):
        f = open('/Users/dracarys983/Crawler/feedlist')
        feeds = f.readlines()[0][0:-1]
        parsed_json = json.loads(feeds)
        urls = [x['url'] for x in parsed_json]
        feedresults = [feedparser.parse(str(x)) for x in urls]

        for feed in feedresults:
            entries = feed['entries']
            for entry in entries:
                title = entry['title'] if 'title' in entry.keys() else 'NA'
                author = entry['author'] if 'author' in entry.keys() else 'NA'
                published = entry['published'] if 'published' in entry.keys() else 'NA'
                summary = entry['summary'] if 'summary' in entry.keys() else 'NA'
                artlink = entry['link'] if 'link' in entry.keys() else 'NA'
                tags = []
                if 'tags' in entry.keys():
                    for tag in entry['tags']:
                        t = Tag.objects.create(
                                term = tag['term'],
                                scheme = '' if tag['scheme'] == None else tag['scheme'],
                                labels = 'NA' if tag['label'] == None else tag['label'],
                                )
                        tags.append(t)
                else:
                    t = Tag.objects.create(
                            term = 'NA',
                            scheme = '',
                            labels = 'NA'
                            )
                    tags.append(t)
                article = NewsArticle.objects.create(
                        title = title,
                        published = published,
                        author = author,
                        summary = summary,
                        link_to_article = artlink,
                        tags = tags)
                article.save()

    def handle(self, **options):
        self._get_articles()
