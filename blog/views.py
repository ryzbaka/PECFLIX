from django.shortcuts import render
from .models import Post,Movie
#from django.http import HttpResponse
def home(request):
	context={
		'posts':Post.objects.all()
	}
	return render(request,'blog/home.html',context)

def about(request):
	return render(request,'blog/about.html',{'title':'About'})
#if the dictionary is small enough then you can pass it as shown in about()
#otherwise pass it in as shown in home

def movies(request):
	Movies={
		'movies':Movie.objects.all()
	}
	return render(request,'blog/movies.html',Movies,{'title':'About'})


