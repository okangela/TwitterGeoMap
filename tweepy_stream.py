import tweepy
import time
import json
from tweepy import OAuthHandler
import os
import sys
import http.client
from elasticsearch import Elasticsearch
import boto3

consumer_key = 'CYt8uVj3H4hyOCPK5oz8iY1CY'
consumer_secret = 'xdI3TdTN9ruQVqu9jWzshqCN3UbPcllrhVtoEfwr1V75n3ix68'
access_token = '115414150-YRHkZ8fGnuCMnfZVoL2eDNtN7MVyRgyeX87scjsT'
access_secret = '2QFLNLQFVag8w7z6gtvvfoxIzmxRtRtY4dMbwPBH1haVm'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

print('Started')
# es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


# sqs = boto3.resource('sqs')
# device_arn = 'arn:aws:sns:us-west-2:453367379586:NewTweet'
# sns = boto3.resource('sns')
# client = boto3.client('sqs')
# queue1 = sqs.get_queue_by_name(QueueName='CloudTweetMap')

# sns = boto3.resource('sns')
client = boto3.client('sns')
# print(queue.url)
# print(queue.attributes.get('DelaySeconds'))
# response = queue.send_message(MessageBody='world')
# print(response.get('MessageId'))
# print(response.get('MD5OfMessageBody'))

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        b = 1
    def on_data(self, data):
        json_data = json.loads(data)
        if( "created_at" in json_data and json_data["lang"] == "en" and json_data["coordinates"] is not None):
            print("Adding tweet id "+str(json_data["id"])+" to Topic")
            tweet_data = {'id':json_data['id_str'],'text':json_data['text'],'user':json_data['user'],'created_at':json_data['created_at'],'coordinates':{'lat':json_data["coordinates"]["coordinates"][1],
        'lng':json_data["coordinates"]["coordinates"][0]}}
            BodyText = 'Tweet '+tweet_data['id']
            sns_input = json.dumps(tweet_data)

            # sns.publish(message=json_data,target_arn=device_arn,message_structure='json')
            client.publish(
                TopicArn='arn:aws:sns:us-west-2:453367379586:NewTweet',
                Message=sns_input,
                Subject=BodyText,
                MessageStructure='string',
                MessageAttributes={
                    'String': {
                        'DataType': 'String',
                        'StringValue': 'string',

                    }
                }
            )
            # parsed_json = str(json_data['_source']['id_str'])
            # print(json_data['id_str'])


            # queue.send_message(tweet_data)
            # queue.send_message(MessageBody='test', MessageAttributes={tweet_data})
            # queue.new_message(tweet_data)
            # BodyText = 'Tweet '+tweet_data['id']


            # print("Adding tweet id "+str(json_data["id"])+" to Elasticsearch")
            # es.index(index="tweetmap", doc_type="tweetdata", body=json_data)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
while True:
    try:
        myStream.sample()
    except Exception as e:
        print(' Error received, retrying in 60 secs')
        print(str(e))
        time.sleep(15)
        # print(str(e))
        pass
