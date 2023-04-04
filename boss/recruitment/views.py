from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
def index(request):
    data = {"code": 0, "msg": "ok"}
    return JsonResponse(data)
    return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse("test1")