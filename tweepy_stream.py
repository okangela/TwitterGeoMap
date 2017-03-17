import tweepy
import time
import json
from tweepy import OAuthHandler
import os
import sys
import http.client
from elasticsearch import Elasticsearch

consumer_key = 'CYt8uVj3H4hyOCPK5oz8iY1CY'
consumer_secret = 'xdI3TdTN9ruQVqu9jWzshqCN3UbPcllrhVtoEfwr1V75n3ix68'
access_token = '115414150-YRHkZ8fGnuCMnfZVoL2eDNtN7MVyRgyeX87scjsT'
access_secret = '2QFLNLQFVag8w7z6gtvvfoxIzmxRtRtY4dMbwPBH1haVm'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

cwd = os.getcwd()
es = Elasticsearch([{'host': 'search-tweetproject-rfj3fbaymnut5knm7e7apux344.us-west-2.es.amazonaws.com', 'port': 80}])

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        b = 1
    def on_data(self, data):
        json_data = json.loads(data)
        if( "created_at" in json_data and json_data["lang"] == "en" and json_data["geo"] is not None):
            print("Adding tweet id "+str(json_data["id"])+" to Elasticsearch")
            es.index(index="tweetmap", doc_type="tweetdata", body=json_data)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
while True:
    try:
        myStream.sample()
    except Exception as e:
        print(' Error received, retrying in 60 secs')
        time.sleep(60)
        print(str(e))
        pass
