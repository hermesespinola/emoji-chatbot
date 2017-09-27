#!/usr/bin/python3
import argparse
import tweepy
import csv
import os

consumer_key = '32qgMUGN2OqjQpB0JSeroN7Jv'
consumer_secret = 'PQF5DGBWSIzM0MmYuOZQbv4ylkNaiAPqDa3qnhd4ZkSztUaR9g'
access_token = '580463560-vLARNL4ZPBHmqigDRQeJcGEBxxBha2ljcGGdffD3'
access_token_secret = 'nYoQx0LkScqdAtFCkKohkCleghtn18ibU0QWjoduy0OU9'

parser = argparse.ArgumentParser(description='Extract tweets from user')
parser.add_argument('--username', '-u', default='TheTweetOfGod',
                    help='username of tweet account to extract its tweets')
parser.add_argument('--max_id', '-m', default=None,
                    help='get tweets below maximum twitter id')
parser.add_argument('--append', '-a', action='store_true',
                    help='get tweets below maximum twitter id')

args = parser.parse_args()
screen_name = args.username
max_id = args.max_id

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
all_tweets = []

print (max_id)
new_tweets = []
if max_id:
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
else:
    new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=int(max_id))
all_tweets.extend(new_tweets)

oldest = all_tweets[-1].id - 1

while len(new_tweets) > 0:
    print ("Getting tweets before {0}".format(oldest))
    new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
    all_tweets.extend(new_tweets)
    oldest = all_tweets[-1].id - 1
    print ("...{0} tweets downloaded so far".format(len(all_tweets)))

out_tweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in all_tweets]

dialect = 'w'
if args.append:
    dialect = 'a'
with open('%s_tweets.csv' % screen_name, dialect) as f:
    writer = csv.writer(f)
    if dialect == 'w':
        writer.writerow(['id','created_at','text'])
    writer.writerows(out_tweets)
