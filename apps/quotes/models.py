from __future__ import unicode_literals

from django.db import models
from ..login.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError

def lengthGreaterThree(value):
    if len(value) < 4:
        raise ValidationError('Must be longer than 3 characters'.format(value))

def lengthGreaterTen(value):
    if len(value) < 10:
        raise ValidationError('Must be longer than 10 characters'.format(value))

class QuoteManager(models.Manager):
    def add_quotes(self, obj, userid, **kwargs):
        user_id = userid
        author = obj['author']
        quote = obj['message']
        user = User.objects.get(id=user_id)
        Quote.objects.create(author=author, message=quote, user=user)
        return {'success': 'Quote created!'}

class Quote(models.Model):
    author = models.CharField(max_length=50, validators=[lengthGreaterThree])
    message = models.TextField(max_length=1000, validators=[lengthGreaterTen])
    user = models.ForeignKey(User, related_name='user_quotes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()

class Fav(models.Model):
    quote = models.ForeignKey(Quote, related_name='fav_quote')
    user = models.ForeignKey(User, related_name='user_fav_quote')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
