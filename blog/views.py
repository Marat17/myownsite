from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('blog index page works!')

def about(request):
	return HttpResponse("here you'll see some info about this blog")

# Create your views here.
