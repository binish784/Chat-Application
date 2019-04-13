
from django.urls import path
from . import views

app_name='chat'

urlpatterns = [
	path('<int:id>',views.showMessage,name='show_message'),
	path('<int:id>/sendMessage',views.sendMessage,name='send_message'),
	path('<int:id>/getMessage',views.getMessage,name='get_message'),
]
