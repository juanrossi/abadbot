# -*- coding: utf-8 -*-
import random

from twitterapi import TwitterAPI
from tweets import tweets

twitter = TwitterAPI()
last_tweets = twitter.timeline('abadbot', 5)


def get_random_tweet():
    return random.choice(tweets)


def get_new_tweet():
    new_tweet = get_random_tweet()
    for tweet in last_tweets:
        # Check if this was posted in one of the last
        # 5 tweets
        if new_tweet.get('text', '') in tweet.text:
            return get_new_tweet()
    return new_tweet


if __name__ == "__main__":
    new_tweet = get_new_tweet()
    if new_tweet.get('type') == 'text':
        twitter.tweet_text(new_tweet.get('text'))
    elif new_tweet.get('type') == 'image':
        twitter.tweet_image(new_tweet.get('image'), new_tweet.get('text'))

    print new_tweet
