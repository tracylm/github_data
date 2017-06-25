from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Hello beautiful!')

def tracy(request):
    return HttpResponse('Hi Tracy!')

def success(request):
    return HttpResponse('Success is near.')
