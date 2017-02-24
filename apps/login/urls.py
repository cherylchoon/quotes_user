from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='user_index'),
    url(r'^register$', register, name='user_register'),
    url(r'^success$', success, name='user_success'),
    url(r'^login$', login, name='user_login'),
    url(r'^logout$', logout, name='user_logout')
]
