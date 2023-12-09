from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

#for yt downloader
from pytube import YouTube

#for weather
import requests
import json

#for gpt
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import GPT4All

template = "Please act as an assistant named Maya. Please provide the answer in a short way. Question: {question}"
prompt = PromptTemplate(template=template, input_variables=["question"])
local_path = ("G:/models/mistral-7b-instruct-v0.1.Q3_K_M.gguf")
llm = GPT4All(model=local_path, backend="gptj", verbose=True)
llm_chain = LLMChain(prompt=prompt, llm=llm)
print("Model loaded :)")




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

def weather(request, city):
    url = f"https://wttr.in/{city}?format=j2"
    # Send a GET request to the URL
    response = requests.get(url)
    # Convert the response text to JSON
    data = json.loads(response.text)
    return JsonResponse(data)

def gpt(request,question):
    # Important string additions for correct processing by Mistral Instruct
    str1 = "###Human:\\n"
    str2 = "\\n###Maya:"
    response = llm_chain.run(str1 + question + str2)
    data={
        'question':question,
        'response':response
    }
    return JsonResponse(data)