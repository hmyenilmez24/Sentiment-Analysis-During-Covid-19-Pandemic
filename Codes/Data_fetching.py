#!/usr/bin/env python
# encoding: utf-8
import tweepy #https://github.com/tweepy/tweepy
import csv

consumer_key= '***********'
consumer_secret= '***********'
access_key= '***********'
access_secret= '***********'
def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []

    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id - 1

    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")
       
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
    
        alltweets.extend(new_tweets)
       
        oldest = alltweets[-1].id - 1
        print(f"...{len(alltweets)} tweets downloaded so far")
  
        outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]

        with open(f'new_{screen_name}_tweets.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["id","created_at","text"])
            writer.writerows(outtweets)
        pass
if __name__ == '__main__':

    get_all_tweets("JOEdotie")
