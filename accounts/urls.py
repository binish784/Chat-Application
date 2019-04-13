

from django.urls import path

import django.contrib.auth.views as auth_views

from . import views

app_name='accounts'

urlpatterns = [
	path('',views.HomeView,name='index'),
	path('all_users/',views.users_list,name='all_users'),
	path('request/<int:id>',views.send_friend_request,name='send_request'),
	path('sentRequests/',views.show_send_requests,name='show_sent'),
	path('cancelRequests/<int:id>',views.cancel_friend_request,name='cancel_sent'),
	path('recieveRequests/',views.show_recieve_requests,name='show_recieve'),
	path('acceptRequest/<int:id>',views.accept_friend_request,name='accept_request'),

	path('login/',auth_views.login,name='login'),
	path('logout/',auth_views.logout,name='logout'),

]
