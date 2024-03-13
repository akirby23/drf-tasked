from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model): 
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=450, blank=True)
    profile_picture = models.ImageField(
        upload_to='images/', default='../default-profile-pic_b6x9hu'
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created: 
        Profile.objects.create(owner=instance, username=instance.username)

post_save.connect(create_profile, sender=User)   
