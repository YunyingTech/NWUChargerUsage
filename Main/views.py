import json

from django.shortcuts import render
from django.shortcuts import HttpResponse

from Main.query import query


# Create your views here.
def index(req):
    return render(req, 'index.html')


def query_all(req):
    print("Start Query All Data.....")
    data = {}
    for id in range(100, 134):
        data.update({id: query('02342' + str(id))})
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def query_by_id(req):
    id = req.GET.get('id')
    print(f"Start Query {id} Data.....")
    data = {}
    data.update({id: query(str(id))})
    return HttpResponse(json.dumps(data, ensure_ascii=False))
