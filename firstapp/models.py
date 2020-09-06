from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Message(models.Model):
    user_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_sender")
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    user_recieve = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_recieve")

    def get_absolute_url(self):
        return reverse('firstapp:message', kwargs={'person_id':self.user_recieve.id})

    def __str__(self):
        return self.user_sender.username
