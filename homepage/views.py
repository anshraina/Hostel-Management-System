from django.shortcuts import render
from django.contrib import messages
# Create your views here.


def index(request):
    storage = messages.get_messages(request)
    return render(request, "indexv2.html", {'messages': storage})

