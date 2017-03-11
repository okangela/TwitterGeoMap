from django.http import HttpResponse
from django.shortcuts import render, redirect
from elasticsearch import Elasticsearch
import json
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def search(request):
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    reqid = request.GET.get('id', '')
    print(reqid)
    jsondata = json.loads(json.dumps(es.get(index='tweetmap', doc_type='tweetdata', id=reqid)))
    # print(jsondata)
    # response = HttpResponse(jsondata, content_type="application/json")
    # print(response)
    return JsonResponse(jsondata)

    # return render('a')
    # return render(request, 'index1.html')
