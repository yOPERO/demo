from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")
    context_dict = {'boldmessage': "I am a bold message", 'italicmessage': "I am an italic message"}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    # return HttpResponse("Rango says: I am the about page! <br/> <a href='/rango/'>Index</a>")
    context_dict = {'aboutmessage': "I am the about message."}
    return render(request, 'rango/about.html', context_dict)

# Create your views here.
