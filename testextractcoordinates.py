import json
import requests
import boto3

# import boto.sqs
# import json


tweet_data = {'id': '853999544723529728', 'text': 'You put the ring upon my finger \nYou put the robe upon my back\nYou throw Your arms around me and… https://t.co/sDXEzD4k5G', 'user': {'id': 2875912923, 'id_str': '2875912923', 'name': 'Stephen Witt', 'screen_name': 'stephenwitt__', 'location': 'MPLS, MN', 'url': 'http://www.stephenwittmusic.com', 'description': '| God | People | Music | ONLINE: latest album on itunes:https://itun.es/us/Cfjf7 FB:stephenwittm\nINSTA:stephenwitt__\nSnapchat:stephenwittmsc', 'protected': False, 'verified': False, 'followers_count': 351, 'friends_count': 275, 'listed_count': 8, 'favourites_count': 1691, 'statuses_count': 1606, 'created_at': 'Fri Nov 14 02:50:56 +0000 2014', 'utc_offset': -18000, 'time_zone': 'Central Time (US & Canada)', 'geo_enabled': True, 'lang': 'en', 'contributors_enabled': False, 'is_translator': False, 'profile_background_color': '000000', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_link_color': '4A913C', 'profile_sidebar_border_color': '000000', 'profile_sidebar_fill_color': '000000', 'profile_text_color': '000000', 'profile_use_background_image': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/764180532452167680/YuK9H3jn_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/764180532452167680/YuK9H3jn_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/2875912923/1471329022', 'default_profile': False, 'default_profile_image': False, 'following': None, 'follow_request_sent': None, 'notifications': None}, 'created_at': 'Mon Apr 17 15:52:12 +0000 2017', 'coordinates': {'lat': 44.98, 'lng': -93.2636}}

# print(tweet_data['id'])
# queue_name = 'CloudTweetMap'
# sqs = boto.sqs.connect_to_region('us-west-2')
# queue = sqs.get_queue(queue_name)
#
# queue.write(queue.new_message(json.loads(str(tweet_data))))

sns = boto3.resource('sns')
client = boto3.client('sns')

print(list(sns.topics.all()))


client.publish(
    TopicArn='arn:aws:sns:us-west-2:453367379586:NewTweet',
    Message=str(tweet_data),
    Subject='Ho ja bhai',
    MessageStructure='string',
    MessageAttributes={
        'String': {
            'DataType': 'String',
            'StringValue': 'string',

        }
    }
)

# print(tweet_data['user']['location'])
#
#
# sqs = boto3.resource('sqs')
# client = boto3.client('sqs')
# queue1 = sqs.get_queue_by_name(QueueName='CloudTweetMap')
# # # for queue in sqs.queues.all():
# # #     print(queue.url)
# #
# queue1.send_message(MessageBody='testuserLocation', MessageAttributes={
#     'UserLoc': {
#         'StringValue': tweet_data['user']['location'],
#         'DataType': 'Number'
#     }
# })

# response = queue1.send_message(MessageBody=tweet_data)

# print(client.get_queue_url(QueueName='CloudTweetMap'))




# res = requests.get('http://localhost:9200')
# r = requests.get('http://localhost:9200/tweetmap/tweetdata/1')
# from elasticsearch import Elasticsearch
# es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# import json
# r = requests.get('http://localhost:9200')
# i = 7000
# while ((requests.get('http://localhost:9200/tweetmap/tweetdata/'+str(i)).status_code) == 200 and i==7000):
#     r = requests.get('http://localhost:9200/tweetmap/tweetdata/'+str(i))
#     # es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
#     # parsed_json = json.loads(json.dumps(es.get(index='tweetmap', doc_type='tweetdata', id=i)))
#     parsed_json_all = json.loads(r.content)
#     parsed_json = parsed_json_all['_source']
#     tweet_data = {'id':parsed_json['id_str'],'text':parsed_json['text'],'user':parsed_json['user'],'created_at':parsed_json['created_at'],'coordinates':{'lat':parsed_json["coordinates"]["coordinates"][1],
# 'lng':parsed_json["coordinates"]["coordinates"][0]}}
#     # print(str(parsed_json['_source']['geo']['coordinates'][0])+','+str(parsed_json['_source']['geo']['coordinates'][1]))
#     # print(parsed_json)
#     # print('\n')
#     # print(parsed_json['user'])
#     print(tweet_data)
#     i=i+1
# print(i)
# print(es.get(index='tweetmap', doc_type='tweetdata', id=i))
# parsed_json = json.loads(json.dumps(es.get(index='tweetmap', doc_type='tweetdata', id=i)))
# print(parsed_json['_source']['id'])
# print(r.content)
