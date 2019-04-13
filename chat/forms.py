from django import forms
from .models import chat


class ChatForm(forms.ModelForm):
	class Meta:
		model=chat
		fields=['message']