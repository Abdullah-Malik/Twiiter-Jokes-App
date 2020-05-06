import tweepy
import time
import csv

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

jokes = []
with open("onelinefun.csv", newline="") as f:
        csvreader = csv.reader(f)
        
        for row in csvreader:
            jokes.append(row[1])

for i in range (len(jokes)):
    api.update_status(jokes[i])
    print(jokes[i])
    time.sleep(2000)
