from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

#from . import forms

from .forms import ProfileUpdateForm, UserViewForm, UserCreateForm
from .models import Profile

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

# SignUp View
class SignUp(CreateView):
	form_class = UserCreateForm
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'



class ProfileUpdateView(LoginRequiredMixin, TemplateView):
	user_form = UserViewForm
	profile_form = ProfileUpdateForm
	template_name = 'accounts/profile-update.html'
	
	def post(self, request):
		
		post_data = request.POST or None
		file_data = request.FILES or None
		
		user_form = UserViewForm(post_data, instance=request.user)
		profile_form = ProfileUpdateForm(post_data, file_data, instance=request.user.profile)
		
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			#messages.success(request, 'Your profile was successfully updated!')
			return HttpResponseRedirect(reverse_lazy('posts:for_user', kwargs={'username': self.request.user.username}))
			
		context = self.get_context_data(user_form=user_form,profile_form=profile_form)
		
		return self.render_to_response(context)
		
	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)



# User Update View
'''
class UserSettings(LoginRequiredMixin, UpdateView):
	template_name = 'accounts/update.html'
	context_object_name = 'user'
	queryset = Profile.objects.all()
	form_class = ProfileUpdateForm
	
	def get_context_data(self, **kwargs):
		context = super(UserSettings, self).get_context_data(**kwargs)
		user = self.request.user
		context['profile_form'] = ProfileUpdateForm(instance=self.request.user.profile, initial={'first_name': user.first_name, 'last_name': user.last_name})
		return context
             
	def form_valid(self, form):
		profile = form.save(commit=False)
		user = profile.user
		user.last_name = form.cleaned_data['last_name']
		user.first_name = form.cleaned_data['first_name']
		user.save()
		profile.save()
		return HttpResponseRedirect(reverse('home'))
'''