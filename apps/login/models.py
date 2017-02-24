from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import bcrypt
import datetime

onlyLetters = RegexValidator(r'^[a-zA-Z ]+$', message='Must be letters only.')
def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError('Must be longer than 2 characters'.format(value))

class UserManager(models.Manager):
    def login(self, object):
        email = object['email']
        password = object['password']
        user = User.objects.get(email=email)
        pw_hash = bcrypt.hashpw(password.encode(), user.password.encode())
        if pw_hash == user.password:
            return {'username': user.alias, 'uid': user.id}
        else:
            return {'error': 'Username/Password does not match.'}

    def register(self, object, **kwargs):
        name = object['name']
        alias = object['alias']
        email = object['email']
        password = object['password']
        birthday = object['birthday_year'] + "-" + object['birthday_month'] + "-" + object['birthday_day']
        print birthday
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(name=name, alias=alias, email=email, password=pw_hash, birthday=birthday)
        user = User.objects.get(email=email)
        return {'success': 'You have registered succesfully!', 'uid': user.id}

class User(models.Model):
    name = models.CharField(max_length=55, validators=[validateLengthGreaterThanTwo, onlyLetters])
    alias = models.CharField(max_length=55, validators=[validateLengthGreaterThanTwo, onlyLetters])
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    birthday = models.DateField(null=True, default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
