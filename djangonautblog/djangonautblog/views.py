from django.http import HttpResponse

def homepage(req):
    return HttpResponse('homepage')

def about(req):
    return HttpResponse('about')
