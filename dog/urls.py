from django.urls import path
from dog.views import *
app_name='dog'

urlpatterns=[
    path('kohli/', kohli ,name='kholi'),
]