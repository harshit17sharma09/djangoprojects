# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)

from django.core.urlresolvers import reverse

from django.views import generic
from groups.Models import Group,GroupMember

class CreateGroup(LoginRequiredMixin,generic.Createview):
    fields = ('name','description')
    model = Group

class SingleGroup(generic.DetailView):
     model =Group
      

class ListGroups(generic.ListView):
    model = Group