from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogPost
from django.template import loader
from django.utils import timezone
from .forms import CreateNewPost

def index(request):
	alltheposts = BlogPost.objects.filter(post_date__lte=timezone.now()).order_by('-post_date')
	context = {
		'alltheposts' : alltheposts,
	}
	return render(request, 'blog/index.html', context)

def about(request):
	return render(request, 'blog/about.html')

def create(request):
	form = CreateNewPost()
	if request.method == 'POST':
		form =CreateNewPost(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)

	return render(request, 'blog/create.html', {'form': form})