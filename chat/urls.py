
from django.urls import path
from . import views

app_name='chat'

urlpatterns = [
	path('<int:id>',views.showMessage,name='show_message'),
	path('<int:id>/sendMessage',views.sendMessage,name='send_message'),
	path('<int:id>/getMessage',views.getMessage,name='get_message'),
	path('showMessage/',views.show_all_Message,name='show_all_messages'),
	path('getAllMessage/',views.get_all_Message,name='get_all_messages'),
]
