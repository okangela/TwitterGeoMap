from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from elasticsearch import Elasticsearch
import json
from django.http import JsonResponse
import requests
from django.core import serializers

def index(request):
    return render(request, 'index.html')

def search(request):
    r = requests.get('http://localhost:9200/tweetmap/tweetdata/_search?q=*')
    parsed_json = json.loads(r.content)
    print(parsed_json['hits']['total'])
    hits = parsed_json['hits']['total']
    outarray = [[]]
    i = 7000
    while (requests.get('http://localhost:9200/tweetmap/tweetdata/'+str(i)).status_code) == 200 and i<=hits:
        r = requests.get('http://localhost:9200/tweetmap/tweetdata/'+str(i))
        parsed_json = json.loads(r.content)
        outarray.append([str(parsed_json['_source']['geo']['coordinates'][0])+','+str(parsed_json['_source']['geo']['coordinates'][1]),parsed_json['_source']['text'],parsed_json['_source']['user']['name']])
        # print(str(parsed_json['_source']['geo']['coordinates'][0])+','+str(parsed_json['_source']['geo']['coordinates'][1]))
        # print(parsed_json['_source']['text'])
        # print(parsed_json['_source']['user']['name'])
        print("success")
        i = i+1
    # es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    # reqid = request.GET.get('q', '')
    # res = es.search(index = 'tweetmap', size=1, body={"query": {"match_all": {}}})

    # print(" response: '%s'" % (res))
    # print(reqid)
    # jsondata = json.loads(json.dumps(es.get(index='tweetmap', doc_type='tweetdata', id=reqid)))
    jsondata = json.dumps(outarray)
    # # print(jsondata)
    # # response = HttpResponse(jsondata, content_type="application/json")
    # # print(response)
    return JsonResponse(outarray, safe=False)

    # return render('a')
    # return render(request, 'index1.html')
    # d = json.dumps(outarray)
    # data = {'d':d}
    # return render_to_response('index.html',data)
    # print(jsondata)
    # return render_to_response('index.html', {'array1': outarray})
