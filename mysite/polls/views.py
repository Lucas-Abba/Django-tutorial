from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    return HttpResponse("Hello, world. You're at the polls index.")
