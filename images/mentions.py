# -*- coding: utf-8 -*-
from twitterapi import TwitterAPI

twitter = TwitterAPI()
search = twitter.search('@abad')

for tweet in search:
    print tweet.text
