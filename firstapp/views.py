from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView, CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.db.models import Q

from firstapp.forms import MessageForm
from firstapp.models import Message
# Create your views here.
class IndexView(TemplateView):
    template_name = 'firstapp/index.html'

class PeopleView(TemplateView):
    template_name = "firstapp/people.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_model'] = User.objects.all()
        return context

class MessageView(CreateView):
    template_name = "firstapp/message.html"
    form_class = MessageForm
    model = Message
    context_object_name = "messages"

    def form_valid(self, form):
        user_recieve_id = self.kwargs.get('person_id')
        form.instance.user_recieve = User.objects.get(id=user_recieve_id)
        form.instance.user_sender = self.request.user
        return super(MessageView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('person_id')
        user_object = User.objects.get(id=user_id)
        login_user = self.request.user
        all_message = Message.objects.filter( Q(user_sender=login_user) | Q(user_sender=user_object), Q(user_recieve=user_object) | Q(user_recieve=login_user)).order_by('pub_date')
        context['all_message'] = all_message
        context['login_user'] = login_user
        context['person'] = User.objects.get(id=user_id)
        return context
