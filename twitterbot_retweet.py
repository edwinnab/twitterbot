import tweepy
from time import sleep
from credetials import*
#access,set and integrate credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#for loop to iterate over the #CodeNewbie and give a limit of 10 people
for tweet in tweepy.Cursor(api.search, q= "#CodeNewbie", since = "2020-06-12", until = "2020-06-13").items(2):
    try:
        print(" \n Tweet by:  @ " + tweet.user.screen_name)
        #retweets the tweets wuth #codenewbie
        tweet.retweet()
        print("retweet using my twitter bot")
        tweet.favorite()
        print("favorite tweet")
        if not tweet.user.following:
            tweet.user.follow()
            print("Followed you")
        sleep(15400)
    except tweepy.TweepError as e:
        print(e.reason("code , code ,code"))
    except StopIteration:
        break


