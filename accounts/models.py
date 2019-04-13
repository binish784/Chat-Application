from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	slug=models.SlugField()
	friends=models.ManyToManyField("Profile",blank=True)

	def __str__(self):
		return self.user.username

def post_save_usermodel_profile(sender,instance,created,*args,**kwargs):
	if created:
		try:
			Profile.objects.create(user=instance)
		except:
			pass

post_save.connect(post_save_usermodel_profile,sender=settings.AUTH_USER_MODEL)

class friendRequest(models.Model):
	to_user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='to_user')
	from_user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='from_user')
	timestamp=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.to_user.username + " - " + self.from_user.username



