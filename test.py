import tweepy
import time 
from credetials import *
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
my_file = open("demo.txt", "r")
file_lines = my_file.readlines()
my_file.close()
def tweet():
    for lines in file_lines:
        try:
            print(lines)
            if lines != "\n":
                api.update_status(lines)
                time.sleep(5)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason("code code code"))
            time.sleep(2)
tweet()