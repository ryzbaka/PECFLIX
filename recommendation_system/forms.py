from django import forms
from django.contrib.auth.models import User
from .models import Reviews
from blog.models import Movie
from django.db import models

class ReviewForm(forms.ModelForm):
    user_id = models.ManyToManyField(User)
    movie_id = models.ManyToManyField(Movie)
    rating=forms.IntegerField(max_value=5)
    class Meta:
        model=Reviews
        fields=['user_id','movie_id','rating']