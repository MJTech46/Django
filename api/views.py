from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from pytube import YouTube
import requests
import json

print("running..")
# Create your views here.
def apiHome(request):
    return HttpResponse('api home')

def ytdownloader(request, url=None):
    #for getting the full like
    query_string = request.GET.urlencode()
    full_url = f'{url}?{query_string}'
    #creating object...
    try:
        youtube = YouTube(full_url)
        streams = youtube.streams
        data = {
            'response':'ok',
        }
        for i, stream in enumerate(streams):
            #you can change the format as you want
            data[i] = {
                        "resolution": stream.resolution, 
                        "mime-type": stream.mime_type, 
                        "download-link": stream.url
            }
    except:
        data={
            'response':"url error"
        }

    return JsonResponse(data)

def weather(request, city=None):
    url = f"https://wttr.in/{city}?format=j2"
    # Send a GET request to the URL
    response = requests.get(url)
    # Convert the response text to JSON
    data = json.loads(response.text)
    return JsonResponse(data)