from django.db import models
from django.contrib.auth.models import User
from blog.models import Movie

class Reviews(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    movie_id=models.ForeignKey(Movie,on_delete=models.CASCADE)
    rating=models.IntegerField()


    def __str__(self):
        return f'{self.user.username} Review'


def save(self):
    super().save()
