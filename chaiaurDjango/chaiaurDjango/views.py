from django.http import HttpResponse;
from django.shortcuts import render;

def home(Request):
    return render(Request, 'website/index.html')

def about(Request):
    return HttpResponse("You are at about page")

def contact(Request):
    return HttpResponse("You are at contact page")