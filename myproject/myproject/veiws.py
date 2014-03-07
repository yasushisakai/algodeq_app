from django.http import HttpResponse

def hello(reques):
    return HttpResponse('Hello world')
