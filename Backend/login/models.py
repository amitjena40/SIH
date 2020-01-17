# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class LoginData(models.Model):
    ident = models.CharField(max_length=240, blank=False, null=False)
    password = models.CharField(max_length=240, blank=False, null=False)
    accessLevel = models.CharField(max_length=240, blank=False, null=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return str(self.ident)

class ResetData(models.Model):
    ident = models.ForeignKey(LoginData, null=True)
    name = models.CharField(max_length=240, blank=False,null=True)
    emailID = models.CharField(max_length=240, blank=False,null=True)
    mobile = models.CharField(max_length=120, blank=False, null=False)
    otp = models.IntegerField(default=0)
    flag = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
