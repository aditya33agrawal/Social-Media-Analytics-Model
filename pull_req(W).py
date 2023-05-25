import tweepy
import csv

# Authenticate to Twitter API
consumerKey = '**************************************'
consumerSecret = '**************************************'
accessToken = '**************************************'
accessTokenSecret = '**************************************'


auth = tweepy.OAuthHandler("consumerKey", "consumerSecret")
auth.set_access_token("accessToken", "accessTokenSecret")

#create  the authentication object
authenticate = tweepy.OAuthHandler(consumerKey , consumerSecret )

#set the access token 
authenticate.set_access_token(accessToken , accessTokenSecret)

#Creating api object
api = tweepy.API(authenticate)

while True:
  keyword = input("Enter the keyword or hashtag to search:")
  noOfTweet = int(input("How many tweets do you want to search:"))

  if keyword == "":
    print("Invalid keyword")
    continue

  tweets = tweepy.Cursor(api.search_tweets , q=keyword).items(noOfTweet)
  tweet_list = []

  for tweet in tweets:
    tweet_list.append(tweet.text)
  break

#checking the length of the list
len(tweet_list)

#saving the extracted tweets in a csv file
import pandas as pd

df = pd.DataFrame(tweet_list)
df.to_csv('output.csv', mode='a', header=False)
