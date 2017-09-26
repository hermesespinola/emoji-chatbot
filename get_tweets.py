#!/usr/bin/python3
import argparse
import tweepy
import csv

consumer_key = '32qgMUGN2OqjQpB0JSeroN7Jv'
consumer_secret = 'PQF5DGBWSIzM0MmYuOZQbv4ylkNaiAPqDa3qnhd4ZkSztUaR9g'
access_token = '580463560-vLARNL4ZPBHmqigDRQeJcGEBxxBha2ljcGGdffD3'
access_token_secret = 'nYoQx0LkScqdAtFCkKohkCleghtn18ibU0QWjoduy0OU9'

parser = argparse.ArgumentParser(description='Extract tweets from user')
parser.add_argument('--username', '-u', default='TheTweetOfGod',
                    help='username of tweet account to extract its tweets')

args = parser.parse_args()
screen_name = args.username

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
all_tweets = []

new_tweets = api.user_timeline(screen_name=screen_name, count=200)
all_tweets.extend(new_tweets)

oldest = all_tweets[-1].id - 1

while len(new_tweets) > 0:
    print ("Getting tweets before {0}".format(oldest))
    new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
    all_tweets.extend(new_tweets)
    oldest = all_tweets[-1].id - 1
    print ("...{0} tweets downloaded so far".format(len(all_tweets)))

out_tweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in all_tweets]

with open('%s_tweets.csv' % screen_name, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id','created_at','text'])
    writer.writerows(out_tweets)
