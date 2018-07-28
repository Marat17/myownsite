from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogPost
from django.template import loader

def index(request):
	alltheposts = BlogPost.objects.order_by('-post_date')
	context = {
		'alltheposts' : alltheposts,
	}
	return render(request, 'blog/index.html', context)

def about(request):
	return render(request, 'blog/about.html')

# Create your views here.
