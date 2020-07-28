from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^(?P<z>[0-9]+)/(?P<x>[0-9]+)/(?P<y>[0-9]+)', views.index, name='index1'),
    # path('', views.index, name='index'),
]