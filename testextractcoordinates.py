import json
import requests
# res = requests.get('http://localhost:9200')
r = requests.get('http://localhost:9200/tweetmap/tweetdata/1')
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# import json
# r = requests.get('http://localhost:9200')
i = 7000
while (requests.get('http://localhost:9200/tweetmap/tweetdata/'+str(i)).status_code) == 200:
    r = requests.get('http://localhost:9200/tweetmap/tweetdata/'+str(i))
    # es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    # parsed_json = json.loads(json.dumps(es.get(index='tweetmap', doc_type='tweetdata', id=i)))
    parsed_json = json.loads(r.content)
    print(str(parsed_json['_source']['geo']['coordinates'][0])+','+str(parsed_json['_source']['geo']['coordinates'][1]))
    i=i+1
# print(i)
# print(es.get(index='tweetmap', doc_type='tweetdata', id=i))
# parsed_json = json.loads(json.dumps(es.get(index='tweetmap', doc_type='tweetdata', id=i)))
# print(parsed_json['_source']['id'])
# print(r.content)
