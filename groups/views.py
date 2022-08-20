from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

from .models import Group, GroupMember
# Create your views here.

"""
# user cannot create new groups
class CreateGroup(LoginRequiredMixin, generic.CreateView):
	model = Group
	fields = ['name', 'description']
	template_name = 'groups/group_form.html'
"""

class SingleGroup(generic.DetailView):
	model = Group

class ListGroup(generic.ListView):
	model = Group