# -*- coding: utf-8 -*-
__author__ = "Tiago Vizoto"
__email__ = "vizoto123@gmail.com"


from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^registro/$', views.register, name='register'),
]