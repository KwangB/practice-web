from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello kb.")
# Create your views here.
