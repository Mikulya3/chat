import profile
from xmlrpc.client import Boolean
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="img", blank=True, null=True)
    friends = models.ManyToManyField('Friend', related_name = "my_friends", blank=True)
    
    def __str__(self):
        return self.name
    

class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.name

class ChatMessage(models.Model):
    body = models.TextField()
    msg_sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="msg_sender")
    msg_receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="msg_receiver")
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.body


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)