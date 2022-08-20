from django.db import models
from django.contrib import auth

# Extending User Model
from django.contrib.auth.models import User as UserModel
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
	
	def __str__(self):
		return "@{}".format(self.username)


# User Profile - One to One Relationship	
class Profile(models.Model):
	NONE = ''
	BEGINNER = 'Beginner'
	INTERMEDIATE = 'Intermediate'
	PRO = 'Pro'
	
	role_level = [
		(NONE, 'NONE'),
		(BEGINNER, 'Beginner'),
		(INTERMEDIATE, 'Intermediate'),
		(PRO, 'Pro'),
	]
	
	# Secondary Information
	user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
	location = models.CharField(max_length=80, blank=True, default='')
	role = models.CharField(max_length=80, blank=True, default='')
	profile_image = models.ImageField(default='default-avatar.png', upload_to='users/', null=True, blank=True)
	level = models.CharField(max_length=12, choices=role_level, default='', null=True)
	
	# Profile Links 
	# Currently Disable - Work Pending
	#website = models.URLField(max_length=200, default='', blank=True)
	#twitter = models.CharField(max_length=40, default='', null=True, blank=True)
	#instagram = models.CharField(max_length=40, default='', null=True, blank=True)
	#facebook = models.CharField(max_length=80, default='', null=True, blank=True)
	
	def __str__(self):
		return "@".format(self.user.username)
		
	
@receiver(post_save, sender=UserModel)
def create_or_update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()