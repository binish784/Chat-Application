from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

# Create your models here.

class chat(models.Model):
	message=models.CharField(max_length=500)
	message_to=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='message_to')
	message_from=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='message_from')
	send_date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return  str(self.message_from) + " - " +str(self.message_to)  + " : " + str(self.message) 