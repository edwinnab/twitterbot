#a program which integrates with the twitter platform
#tweets from a file
#retweets, follows and favorites
import tweepy
#importin a specific time module
from time import sleep
#import credentials from the credentials file
from credetials import *
#access our twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#open file for reading
my_file = open("verne.txt", "r")
#read line by line and assign to a variable
file_lines = my_file.readlines()
#close files
my_file.close()
#loop to display the lines from our text file
def tweet():
    for line in file_lines:
        #catches the duplicate error
        try:
            print(line)
            #if statement to skip over the blank lines
            if line != "\n":
                api.update_status(line)
                sleep(7200)
            else:
                pass 
        except tweepy.TweepError as e:
            print(e.reason("code code code"))
        #sleep() only works with seconds 
            sleep(1800)
tweet()
