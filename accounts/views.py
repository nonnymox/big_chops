from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def register_user(request):
    return HttpResponse("User Reg Form")