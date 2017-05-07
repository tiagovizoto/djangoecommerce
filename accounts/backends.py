# -*- coding: utf-8 -*-
__author__ = "Tiago Vizoto"
__email__ = "vizoto123@gmail.com"

from django.contrib.auth.backends import ModelBackend as BaseModelBackend


class ModelBackend(BaseModelBackend):

    def authenticate(self, username=None, password=None):

        pass