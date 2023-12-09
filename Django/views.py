from django.shortcuts import render
from django.urls import get_resolver

# Create your views here.
def purify_links(url):
    #for url
    if '(?P<url>.+)' in url:
        url = url.split('/') #converting to list
        url = url[:-2]+['<url>']
        new_url=''
        for i in url:
            new_url=new_url+i+'/'
        return new_url
    #for city
    elif '(?P<city>[^/]+)' in url:
        url = url.split('/')
        url = url[:2]+['<city>']
        new_url=''
        for i in url:
            new_url=new_url+i+'/'
        return new_url
    #for question
    elif '(?P<question>[^/]+)' in url:
        url = url.split('/')
        url = url[:2]+['<question>']
        new_url=''
        for i in url:
            new_url=new_url+i+'/'
        return new_url
    #if None
    else:
        return url

def get_all_links(request):
    urls = set(v[1].replace('\\Z', '') for k,v in get_resolver(None).reverse_dict.items()) #collecting all liks 
    urls.remove('') #removing home url
    print(urls)
    urls = map(purify_links,urls) #removing unwanded things like (?P<url>.+)
    return render(request, 'Django/index.html',{'urls':urls})
