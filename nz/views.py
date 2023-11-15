from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def williamson(request):
    return HttpResponse('<h1>good captain in newzealand/h1>')

def ravindra(request):
    return HttpResponse('<h1> super youngplayer  player in newzeland</h1>')
