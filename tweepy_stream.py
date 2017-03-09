import tweepy
import json
from tweepy import OAuthHandler
import os
import sys

consumer_key = 'CYt8uVj3H4hyOCPK5oz8iY1CY'
consumer_secret = 'xdI3TdTN9ruQVqu9jWzshqCN3UbPcllrhVtoEfwr1V75n3ix68'
access_token = '115414150-YRHkZ8fGnuCMnfZVoL2eDNtN7MVyRgyeX87scjsT'
access_secret = '2QFLNLQFVag8w7z6gtvvfoxIzmxRtRtY4dMbwPBH1haVm'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

cwd = os.getcwd()
json_file_1 = cwd + "/output1.json"

# def write_tweets(tweet, filename):
#     with open(filename, 'a') as f:
#             json.dump(tweet, f)
#             f.write('\n')
#     with open('file.txt', 'a') as f:
#         print(data, file=f)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        b = 1
    def on_data(self, data):
        json_data = json.loads(data)
        if( "created_at" in json_data and json_data["lang"] == "en" and json_data["geo"] is not None):
            print("Adding tweet id "+str(json_data["id"])+" to file output.json")
            with open(json_file_1, 'a') as f:
                print(data, file=f)

            #  write_tweets(data, json_file_1)
            #  print(json_data["user"]["name"] +','+str(json_data["geo"]["coordinates"][0])+":"+str(json_data["geo"]["coordinates"][1])+", "+json_data["place"]["country_code"]+":"+json_data["place"]["country"])
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.sample()
