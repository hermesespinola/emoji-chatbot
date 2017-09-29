#!/usr/bin/python
import argparse
import tweepy
import jsonpickle
import csv
import os

consumer_key = '32qgMUGN2OqjQpB0JSeroN7Jv'
consumer_secret = 'PQF5DGBWSIzM0MmYuOZQbv4ylkNaiAPqDa3qnhd4ZkSztUaR9g'

parser = argparse.ArgumentParser(description='Extract tweets from user')
parser.add_argument('--username', '-u', default='TheTweetOfGod',
                    help='username of tweet account to extract its tweets')

args = parser.parse_args()
searchQuery = '@' + args.username
maxTweets = 400

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
auth.secure = True
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
retweet_filter='-filter:retweets'
max_id = -1L
q=searchQuery+retweet_filter
tweetsPerQry = 100
fName = 'tweets.txt'
sinceId = None

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
with open(fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
		if (not tweet._json['retweeted']) and ('RT @' not in tweet._json['text']):
                	f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        	'\n')
            		tweetCount += 1
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))
