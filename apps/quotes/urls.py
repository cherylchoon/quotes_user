from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^quotes$', index, name='quotes_index'),
    url(r'^quotes/add_quotes$', add_quotes, name='add_quotes'),
    url(r'^quotes/add_fav$', add_fav, name='add_fav'),
    url(r'^quotes/delete_fav$', delete_fav, name='delete_fav'),
    url(r'^users/(?P<id>\d+)$', user_info, name='user_info'),

]
