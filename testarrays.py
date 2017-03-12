import json
import requests
reqid = 'trump'
r = requests.get('http://localhost:9200/tweetmap/tweetdata/_search?q='+str(reqid))
parsed_json = json.loads(r.content)
parsed_json2 = json.dumps(parsed_json['hits']['hits'])
print(parsed_json2[20])
