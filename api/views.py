from django.shortcuts import render, HttpResponse

# Create your views here.
def apiHome(request):
    return HttpResponse('api home')