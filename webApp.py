from django.shortcuts import HttpResponse

def index(request):
  html = "<H1>People</H1><HR>"
  return HttpResponse(html)