from django.shortcuts import render,get_object_or_404
from django.conf import settings

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.

from .models import Profile,friendRequest


@login_required
def HomeView(request):
	user_profile=Profile.objects.get(user=request.user)
	connected=user_profile.friends.all()
	context={
		'friends':connected
	}
	return render(request,'accounts/home.html',context)

def users_list(request):
	user_profile=Profile.objects.get(user=request.user)
	users=Profile.objects.filter().exclude(profile=user_profile).exclude(user=request.user)
	context={
		'all_users':users,
	}
	return render(request,'accounts/all_users.html',context)

def show_send_requests(request):
	requests=friendRequest.objects.filter(from_user=request.user)
	context={
		'requests':requests,
	}
	return render(request,'accounts/sentRequest.html',context)

def show_recieve_requests(request):
	requests=friendRequest.objects.filter(to_user=request.user)
	context={
		'requests':requests,
	}
	return render(request,'accounts/recieveRequest.html',context)

def send_friend_request(request,id):
	to_user=get_object_or_404(User,id=id)
	from_user=request.user
	frequest,created=friendRequest.objects.get_or_create(
		from_user=from_user,
		to_user=to_user
		)
	return HttpResponseRedirect('/')

def cancel_friend_request(request,id):
	to_user=get_object_or_404(User,id=id)
	frequest=friendRequest.objects.get(
		to_user=to_user,
		from_user=request.user
		)
	frequest.delete()
	return HttpResponseRedirect('/')

def accept_friend_request(request,id):
	user1=get_object_or_404(User,id=id)
	user2=request.user
	frequest=friendRequest.objects.filter(to_user=user2,from_user=user1).first()
	user1_profile=Profile.objects.get(user=user1)
	user2_profile=Profile.objects.get(user=user2)
	user1_profile.friends.add(user2_profile)
	user2_profile.friends.add(user1_profile)
	frequest.delete()
	return HttpResponseRedirect('/')


def unfriend_user(request,id):
	selected_user=get_object_or_404(User,id=id)
	user1_profile=Profile.objects.get(user=request.user)
	user2_profile=Profile.objects.get(user=selected_user)
	user1_profile.friends.remove(user2_profile)
	user2_profile.friends.remove(user1_profile)
	return HttpResponseRedirect('/')

def user_profile(request,id):
	selected_user=get_object_or_404(User,id=id)
	context={
		'selected_user':selected_user,
	}
	return render(request,'accounts/profile.html',context)