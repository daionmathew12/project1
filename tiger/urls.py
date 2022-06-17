from django.urls import path
from tiger.views import *
app_name='tiger'

urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
]