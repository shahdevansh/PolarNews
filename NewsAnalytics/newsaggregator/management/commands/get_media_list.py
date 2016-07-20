from django.core.management.base import NoArgsCommand
from newsaggregator.models import MediaSource
import json, mediacloud, requests

class Command(NoArgsCommand):
    def _get_media_list(self):
        media = []
        start = 0
        rows  = 100
        it = 0
        f = open('/Users/dracarys983/Crawler/medialist', 'w')
        while True:
            params = { 'start': start, 'rows': rows, 'key': '2a21c8adcec21081e6b3d31c35a7e89da6d70eede9c40225d42ffe987ba8c709' }
            r = requests.get( 'https://api.mediacloud.org/api/v2/media/list', params = params, headers = { 'Accept': 'application/json'} )
            data = r.json()
            it += 1

            if len(data) == 0:
                break

            start += rows
            media.extend(data)

            if(it == 250):
                break

        json.dumps(media, f)
        f.close()
        for source in media:
            entry = MediaSource.objects.create(
                        media_id = source['media_id'],
                        link_to_source = source['url'],
                        name = source['name']
                        )
            entry.save()

    def handle(self, **options):
        self._get_media_list()
