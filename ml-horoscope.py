import tweepy

consumer_key = open("consumer_key", "r")
consumer_secret = open("consumer_secret", "r")
access_token = open("access_token", "r")
access_token_secret = open("access_secret", "r")

auth = tweepy.OAuthHandler(consumer_key.read(), consumer_secret.read())
auth.set_access_token(access_token.read(), access_token_secret.read())

api = tweepy.API(auth)

