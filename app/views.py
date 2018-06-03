from django.shortcuts import render
import requests
import json

from django.shortcuts import render, HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test(request):
    return HttpResponse('My second view')

def profile(request):
    jsonList = []
    req = requests.get('https://api.github.com/users/DrkSephy')
    jsonList.append(json.loads(req.text))
    parsedData = []
    userData = {}
    for data in jsonList:
        userData['name'] = data['name']
        userData['blog'] = data['blog']
        userData['email'] = data['email']
        userData['public_gists'] = data['public_gists']
        userData['public_repos'] = data['public_repos']
        userData['avatar_url'] = data['avatar_url']
        userData['followers'] = data['followers']
        userData['following'] = data['following']
    parsedData.append(userData)
    return render(request, 'app/profile.html',  {'data': parsedData})