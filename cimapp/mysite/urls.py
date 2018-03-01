from django.conf.urls import url
from .views import home, register, dash, userdash, auth_dash

urlpatterns = [
    url(r'^$', home),
    url(r'^register/', register),
    url(r'^authdash/', auth_dash),
    url(r'^dash/', dash, name='dash'),
    url(r'^userdash/', userdash, name='userdash'),
]
