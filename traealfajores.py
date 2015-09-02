import json

from tweepy.streaming import StreamListener
from tweepy import Stream
from twitterapi import TwitterAPI

twitter = TwitterAPI()


class TraeAlfajoreListener(StreamListener):
    """
    A listener handles to handle tweets from Ezeiza
    """
    def on_data(self, data):
        twitter.tweet_text('Trae alfajores!', json.loads(data).get('id'))
        return True

    def on_error(self, status):
        if status == 420:
            return False

    def on_timeout(self):
        print 'Timeout...'
        return True  # Don't kill the stream


if __name__ == '__main__':
    l = TraeAlfajoreListener()

    stream = Stream(twitter.auth, l)
    stream.filter(track=['Aeropuerto Internacional de Ezeiza - Ministro Pistarini'])
