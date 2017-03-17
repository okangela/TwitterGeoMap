import json, time
import requests
from elasticsearch import Elasticsearch
from datetime import datetime
reqid = 'trump'
r = requests.get('http://localhost:9200/tweetmap/tweetdata/_search?size=1000&q='+str(reqid))
parsed_json = json.loads(r.content)
hits = parsed_json['hits']['total']
i = 0
es = Elasticsearch([{'host': 'search-tweetproject-rfj3fbaymnut5knm7e7apux344.us-west-2.es.amazonaws.com', 'port': 80}])

# def demo_bad_catch():
#     while True:
#         try:
#             raise ValueError('represents a hidden bug, do not catch this')
#             raise Exception('This is the exception you expect to handle')
#         except Exception as e:
#             time.sleep(5)
#             demo_bad_catch()
#             print('caught this error: '+str(e))
#
# demo_bad_catch()

# from elasticsearch import Elasticsearch, RequestsHttpConnection
# from requests_aws4auth import AWS4Auth

# host = 'search-tweetproject-rfj3fbaymnut5knm7e7apux344.us-west-2.es.amazonaws.com'
# awsauth = AWS4Auth(YOUR_ACCESS_KEY, YOUR_SECRET_KEY, REGION, 'es')
#
# es = Elasticsearch(
#     hosts=[{'host': host, 'port': 443}],
#     http_auth=awsauth,
#     use_ssl=True,
#     verify_certs=True,
#     connection_class=RequestsHttpConnection
# )



# while(i == 0):
print(parsed_json['hits']['hits'][0]['_source']['coordinates']['coordinates'])
    # i = i+1
    # print(parsed_json['hits']['hits'][i]['_source']['geo']['coordinates'][1])
    # print(parsed_json['hits']['hits'][i]['_source']['user']['name'])
    # print(parsed_json['hits']['hits'][i]['_source']['text'])

    # outarray.append([parsed_json['hits']['hits'][i]['_source']['geo']['coordinates'][0],parsed_json['hits']['hits'][i]['_source']['geo']['coordinates'][1],parsed_json['hits']['hits'][i]['_source']['text'],parsed_json['hits']['hits'][i]['_source']['user']['name']])

    # i += 1
# # # parsed_json2 = json.dumps(parsed_json['hits']['hits'])
# # # print(parsed_json['hits']['hits'][3])
#
# # entry = {'id': 1,
# #     'title': 'First post!',
# #     'content': '<p>First post!</p>',
# #     'tags': ['status', 'blog'],
# #     'created': '20130423T16:50:22'
# #     }
# #
# # es.index(index='blog-index', doc_type='blog-entry-type', body=entry)
# data = json.loads({"created_at":"Sun Mar 12 21:31:00 +0000 2017","id":841038843365249025,"id_str":"841038843365249025","text":"I'm Just Sayin!\n\n#fakepresident I'm back! #notapaidprotestor \nYour first 50 days have been\u2026 https:\/\/t.co\/84Qp9ZWlng","source":"\u003ca href=\"http:\/\/instagram.com\" rel=\"nofollow\"\u003eInstagram\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":457871777,"id_str":"457871777","name":"Leverage_CR","screen_name":"leverage_cr","location":"Yonkers, NY","url":"http:\/\/leveragecreditrecovery.com\/","description":"Teaching Business Mindset for Personal Empowerment","protected":false,"verified":false,"followers_count":2280,"friends_count":2180,"listed_count":135,"favourites_count":5815,"statuses_count":51196,"created_at":"Sat Jan 07 22:41:08 +0000 2012","utc_offset":-25200,"time_zone":"Pacific Time (US & Canada)","geo_enabled":true,"lang":"en","contributors_enabled":false,"is_translator":false,"profile_background_color":"4A913C","profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/574529496931418114\/zyXKocBZ.png","profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/574529496931418114\/zyXKocBZ.png","profile_background_tile":true,"profile_link_color":"3B94D9","profile_sidebar_border_color":"000000","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/802910148180279298\/tLcGfOkb_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/802910148180279298\/tLcGfOkb_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/457871777\/1483212967","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":{"type":"Point","coordinates":[40.9538378,-73.8957989]},"coordinates":{"type":"Point","coordinates":[-73.8957989,40.9538378]},"place":{"id":"b87b05856ab8dbd8","url":"https:\/\/api.twitter.com\/1.1\/geo\/id\/b87b05856ab8dbd8.json","place_type":"city","name":"Yonkers","full_name":"Yonkers, NY","country_code":"US","country":"United States","bounding_box":{"type":"Polygon","coordinates":[[[-73.911271,40.900789],[-73.911271,40.988346],[-73.810443,40.988346],[-73.810443,40.900789]]]},"attributes":{}},"contributors":null,"is_quote_status":false,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[{"text":"fakepresident","indices":[17,31]},{"text":"notapaidprotestor","indices":[42,60]}],"urls":[{"url":"https:\/\/t.co\/84Qp9ZWlng","expanded_url":"https:\/\/www.instagram.com\/p\/BRjaC8EDW5D\/","display_url":"instagram.com\/p\/BRjaC8EDW5D\/","indices":[92,115]}],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"en","timestamp_ms":"1489354260661"})
# print(data)
#
# es.index(index="abcdefgh123", doc_type="abcdefgh-type123", body={"any": "data", "timestamp": datetime.now()})
# # print(es.get(index="abcdefgh123", doc_type="abcdefgh-type123", id=2)['_source'])
