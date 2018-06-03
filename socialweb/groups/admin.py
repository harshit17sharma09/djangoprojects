# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from . import models

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)