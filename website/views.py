from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import requests

# Create your views here.

def home(request):
    if request.method == 'GET':
        try:
            word = request.GET.get('word')
            r = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}')
            a = r.json()

            answer = a[0]['meanings'][0]['definitions'][0]['definition']
            return render(request, 'website/home.html', {'a':answer})
        except:
            return render(request, 'website/home.html', {'a':'Word does not exist'})


    return HttpResponse('website/home.html')