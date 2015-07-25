# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Device(models.Model):
    device_id = models.CharField(max_length=100, unique=True)
    push_token = models.CharField(max_length=190)
    user_name = models.CharField(max_length=30, null=False, blank=False)


class Talk(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=30)
    content = models.CharField(max_length=1000, null=False, blank=False)

    class Meta:
        ordering = ('created',)
