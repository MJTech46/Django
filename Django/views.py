from django.shortcuts import render
from django.urls import get_resolver

# Create your views here.
def getAllLinks(request):
    urls = set(v[1].replace('\\Z', '') for k,v in get_resolver(None).reverse_dict.items()) #collecting all liks 
    urls.remove('') #removing home url
    return render(request, 'Django/index.html',{'urls':urls})
