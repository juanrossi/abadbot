import tweepy
import settings


class TwitterAPI:
    """Base class to wrap tweepy methods"""
    auth = None

    def __init__(self):
        self.auth = tweepy.OAuthHandler(settings.CONSUMER_KEYS, settings.CONSUMER_SECRET)
        self.auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)

    def tweet_text(self, message, reply_id=None):
        self.api.update_status(status=message, in_reply_to_status_id=reply_id)

    def tweet_image(self, filename, status=''):
        self.api.update_with_media('images/{}'.format(filename), status)

    def timeline(self, user, count=5):
        return self.api.user_timeline(screen_name=user, count=count)

    def search(self, q, limit=50):
        return self.api.search(q, rpp=limit)
