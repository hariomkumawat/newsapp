from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    # api_request = requests.get("http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=b910d1f00d0f4f4b8a4be92cbdb6bb50")
    # api_request = requests.get("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=619c926ec7c8445ea1ec2064c0bd5464")
    api_request= requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=619c926ec7c8445ea1ec2064c0bd5464")
    # api_request= requests.get("https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=619c926ec7c8445ea1ec2064c0bd5464")
    # api_request=
    # api_request=
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api' : api})