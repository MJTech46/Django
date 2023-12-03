from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from pytube import YouTube

# Create your views here.
def apiHome(request):
    return HttpResponse('api home')

def ytdownloader(request, url):
    #for getting the full like
    query_string = request.GET.urlencode()
    full_url = f'{url}?{query_string}'
    #creating object...
    try:
        youtube = YouTube(full_url)
        streams = youtube.streams
        data = {}
        for i, stream in enumerate(streams):
            #you can change the format as you want
            data[i] = {
                        "resolution": stream.resolution, 
                        "mime-type": stream.mime_type, 
                        "download-link": stream.url
            }
    except:
        data= {
            "info": "invalid link"
        }
        
    return JsonResponse(data)
