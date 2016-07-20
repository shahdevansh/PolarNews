import mediacloud, json, datetime
mc = mediacloud.api.MediaCloud('2a21c8adcec21081e6b3d31c35a7e89da6d70eede9c40225d42ffe987ba8c709')

num_feeds = 20
last_feed_id = 19
media_id = 1
feeds = mc.feedList(media_id, last_feed_id, num_feeds)
print json.dumps(feeds)
