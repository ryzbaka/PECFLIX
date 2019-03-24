from django.urls import path
from . import views

urlpatterns=[
	path('',views.home,name='blog-home'),
	path('about/',views.about,name='blog-about'),
	path('movies/',views.movies,name='pecflix-movies')
]
