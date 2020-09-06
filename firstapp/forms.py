from django import forms
from django.forms import ModelForm, HiddenInput
from django.contrib.auth.models import User

from firstapp.models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('text',)
