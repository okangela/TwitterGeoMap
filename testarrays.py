import json
import requests
reqid = 'trump'
r = requests.get('http://localhost:9200/tweetmap/tweetdata/_search?size=1000&q='+str(reqid))
parsed_json = json.loads(r.content)
hits = parsed_json['hits']['total']
i = 0

while(i < hits):
    print(parsed_json['hits']['hits'][i]['_source']['geo']['coordinates'][0])
    print(parsed_json['hits']['hits'][i]['_source']['geo']['coordinates'][1])
    print(parsed_json['hits']['hits'][i]['_source']['user']['name'])
    print(parsed_json['hits']['hits'][i]['_source']['text'])

    # outarray.append([parsed_json['hits']['hits'][i]['_source']['geo']['coordinates'][0],parsed_json['hits']['hits'][i]['_source']['geo']['coordinates'][1],parsed_json['hits']['hits'][i]['_source']['text'],parsed_json['hits']['hits'][i]['_source']['user']['name']])

    i += 1
# parsed_json2 = json.dumps(parsed_json['hits']['hits'])
# print(parsed_json['hits']['hits'][3])
