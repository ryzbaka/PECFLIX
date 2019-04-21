from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Reviews

@receiver(post_save,sender=User)
def create_review(sender,instance,created, **kwargs):
    if created:
        Reviews.objects.create(user_id=instance)


@receiver(post_save,sender=User)
def save_review(sender,instance,created, **kwargs):
    instance.profile.save()